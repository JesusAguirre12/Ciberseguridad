from pwn import *
import binascii
import time
import os

# Forzar a pwntools a ser silencioso con las aperturas/cierres de sockets
context.log_level = 'error'

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

def is_good_key(ob, possible_key):
    for i in range(256):
        if ob[i] != Sbox[possible_key ^ i] % 2:
            return False
    return True

def get_leakage_with_retry(p1):
    for intento in range(3):
        try:
            r = remote('saturn.picoctf.net', 59220)
            r.recvuntil(b':')
            r.sendline(p1.hex().encode())
            response = r.recvline().strip()
            r.close()
            
            if b":" in response:
                numero_limpio = response.split(b":")[-1].strip()
            else:
                numero_limpio = response
                
            return int(numero_limpio)
        except (EOFError, ValueError, PwnlibException):
            time.sleep(0.2)
            continue
    raise RuntimeError("El servidor falló repetidamente tras 3 intentos.")

def find_key():
    print("[*] Iniciando el ataque de Análisis de Energía...")
    final_key = []
    log_filename = "progreso_key.txt"
    
    # --- NUEVO: REANUDAR PROGRESO DESDE EL TXT ---
    if os.path.exists(log_filename):
        print(f"[*] Detectado archivo '{log_filename}'. Intentando recuperar progreso...")
        with open(log_filename, "r") as f:
            lines = f.readlines()
        
        # Buscar la última línea que contenga una llave parcial válida
        last_partial_line = None
        for line in reversed(lines):
            if "Llave parcial:" in line:
                last_partial_line = line
                break
                
        if last_partial_line:
            hex_part = last_partial_line.split("Llave parcial:")[-1].strip()
            if hex_part:
                # Convertir el string hex (ej: "4aef23") de vuelta a lista de enteros
                final_key = [int(hex_part[i:i+2], 16) for i in range(0, len(hex_part), 2)]
                print(f"[+] Progreso recuperado exitosamente. Saltando a la posición de byte: {len(final_key)}")
    else:
        # Si no existe, crear el archivo limpio
        with open(log_filename, "w") as f:
            f.write("--- INICIO DE ATAQUE DE ANÁLISIS DE ENERGÍA ---\n")

    # Empezar el bucle desde donde se quedó el progreso (len(final_key))
    for byte_pos in range(len(final_key), 16):
        ob = [0] * 256
        print(f"[*] Atacando la posición del byte: {byte_pos}...")
        
        for i in range(256):
            p1 = b'\x00' * byte_pos + bytes([i]) + b'\x00' * (15 - byte_pos)
            
            try:
                ob[i] = get_leakage_with_retry(p1)
            except RuntimeError as e:
                print(f"\n[-] Error crítico en byte {byte_pos}, índice {i}: {e}")
                return None
                
        ob_min = min(ob)
        ob_minus_min = [x - ob_min for x in ob]
        
        for possible_key in range(256):
            if is_good_key(ob_minus_min, possible_key):
                final_key.append(possible_key)
                
                with open(log_filename, "a") as f:
                    f.write(f"Byte {byte_pos:02d} encontrado: {hex(possible_key)} | Llave parcial: {''.join(f'{k:02x}' for k in final_key)}\n")
                
        print(f"[+] Progreso en vivo (Hex): {''.join(f'{k:02x}' for k in final_key)}")
        
    return final_key

key = find_key()
if key:
    hex_key = "".join(f"{h:02x}" for h in key)
    
    # --- NUEVO: CONVERTIR DE HEX / INT A FORMATO TEXTO NORMAL ---
    try:
        normal_key = bytes(key).decode('utf-8', errors='ignore')
    except Exception:
        normal_key = "".join(chr(b) if 32 <= b <= 126 else '?' for b in key)
        
    print("\n" + "="*40)
    print(f"[+] ¡Llave completa encontrada (Hex)!: {hex_key}")
    print(f"[+] ¡FLAG / TEXTO EN FORMATO NORMAL!:  {normal_key}")
    print("="*40)
    
    with open("progreso_key.txt", "a") as f:
        f.write(f"\n[+] LLAVE FINAL COMPLETA (Hex): {hex_key}\n")
        f.write(f"[+] FLAG EN FORMATO NORMAL: {normal_key}\n")
