#!/usr/bin/env python3

def rc4_crypt(key: bytes, data: bytes) -> bytes:
    """Cifrado/Descifrado RC4 clásico (Muy habitual en retos de reversing/malware)."""
    S = list(range(256))
    j = 0
    out = []
    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    # Pseudo-random Generation Algorithm (PRGA)
    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)

def custom_rolling_xor(data: bytes, key_byte: int) -> bytes:
    """Aplica un XOR dinámico donde la clave varía según el byte anterior."""
    res = []
    current_key = key_byte
    for b in data:
        res.append(b ^ current_key)
        current_key = (current_key + b) % 256  # Mutación común de clave
    return bytes(res)

def z3_keygen_blueprint():
    """
    Blueprint de referencia para resolver restricciones de ecuaciones (Keygens) usando Z3.
    Copia y pega este fragmento cuando requieras forzar condiciones lógicas complejas.
    """
    blueprint = """
    from z3 import *
    s = Solver()
    # Definir variables (Ej: password de 4 bytes)
    flag = [BitVec(f'flag_{i}', 8) for i in range(4)]
    
    # Añadir restricciones de caracteres imprimibles
    for f in flag:
        s.add(f >= 32, f <= 126)
        
    # Ecuaciones dadas por la ingeniería inversa del binario
    s.add(flag[0] ^ flag[1] == 0x42)
    s.add(flag[2] + flag[3] == 150)
    s.add(flag[0] * 2 - flag[2] == 80)
    
    if s.check() == sat:
        m = s.model()
        print("Flag encontrada: " + "".join([chr(m[f].as_long()) for f in flag]))
    else:
        print("Imposible de resolver (Unsat)")
    """
    print(blueprint)
