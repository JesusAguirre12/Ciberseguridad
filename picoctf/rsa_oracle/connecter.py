from pwn import *
from Cryptodome.Util.number import long_to_bytes

# Tu puerto
r = remote('titan.picoctf.net', 54272)

def encrypt_2():
    r.sendlineafter(b'what should we do for you?', b'E')
    # ENVIAMOS EL BYTE \x02, NO EL STRING "02"
    r.sendlineafter(b'enter text to encrypt', b'\x02')
    r.recvuntil(b'ciphertext (m ^ e mod n) ')
    
    # EL SERVIDOR DEVUELVE DECIMAL (base 10), NO HEX
    line = r.recvline().decode().strip()
    return int(line) 

def decrypt(c):
    r.sendlineafter(b'what should we do for you?', b'D')
    # AQUÍ ESTABA EL CRASH: HAY QUE ENVIAR DECIMAL (str), NO HEX (hex)
    r.sendlineafter(b'Enter text to decrypt: ', str(c).encode())
    
    r.recvuntil(b'hex (c ^ d mod n):')
    line = r.recvline().decode().strip()
    # ESTO SÍ LO DEVUELVE EN HEX
    return int(line, 16)

# Tu password.enc
C_TARGET = 4228273471152570993857755209040611143227336245190875847649142807501848960847851973658239485570030833999780269457000091948785164374915942471027917017922546

print("[*] 1. Pidiendo al oráculo que encripte el byte \\x02...")
c2 = encrypt_2()

print("[*] 2. Multiplicando C_TARGET * c2...")
c_blind = C_TARGET * c2 

print("[*] 3. Pidiendo al oráculo que desencripte nuestro engendro...")
m_blind = decrypt(c_blind)

print("[*] 4. Dividiendo entre 2 para sacar la password real...")
m = m_blind // 2

# Convertimos a ASCII
password = long_to_bytes(m)
print(f"\n[+] ¡PASSWORD RECUPERADA!: {password.decode('ascii')}")

r.close()
