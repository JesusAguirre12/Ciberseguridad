#!/usr/bin/env python3
import math
import random
from functools import reduce
from Cryptodome.Cipher import AES, DES
from Cryptodome.Util.number import bytes_to_long, long_to_bytes, inverse

def pollard_rho(n, max_steps=1000000):
    """Factoriza N si tiene factores medianos/pequeños."""
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    x, y, c, g = random.randint(2, n - 1), random.randint(2, n - 1), random.randint(1, n - 1), 1
    f = lambda x: (pow(x, 2, n) + c) % n
    steps = 0
    while g == 1 and steps < max_steps:
        x = f(x)
        y = f(f(y))
        g = math.gcd(abs(x - y), n)
        steps += 1
    return g if g != n else None

def p_minus_1_attack(n, B=100000):
    """Ataque P-1 de Pollard si (p-1) está compuesto por primos pequeños."""
    primes = []
    is_prime = [True] * (B + 1)
    for p in range(2, B + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, B + 1, p): is_prime[i] = False
    a = 2
    for p in primes:
        exponent = int(math.log(B) / math.log(p))
        a = pow(a, pow(p, exponent), n)
    g = math.gcd(a - 1, n)
    return g if 1 < g < n else None

def fermat_factor(n):
    """Factoriza N si p y q están muy cerca en la recta numérica."""
    a = math.isqrt(n) + 1
    b2 = a*a - n
    while not math.isqrt(b2)**2 == b2:
        a += 1
        b2 = a*a - n
    p = a - math.isqrt(b2)
    q = a + math.isqrt(b2)
    return p, q

def wiener_attack(e, n):
    """Destroza RSA si el exponente privado 'd' es muy pequeño (d < 1/3 * N^(1/4))."""
    def continued_fraction(n, d):
        cf = []
        while d:
            cf.append(n // d)
            n, d = d, n % d
        return cf
    def convergents(cf):
        convs = []
        p1, q1, p2, q2 = 1, 0, cf[0], 1
        convs.append((p2, q2))
        for i in range(1, len(cf)):
            p = cf[i] * p2 + p1
            q = cf[i] * q2 + q1
            convs.append((p, q))
            p1, q1, p2, q2 = p2, q2, p, q
        return convs
    cf = continued_fraction(e, n)
    convs = convergents(cf)
    for k, d in convs:
        if k == 0: continue
        if (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            b = n - phi + 1
            discr = b*b - 4*n
            if discr >= 0:
                r = math.isqrt(discr)
                if r*r == discr and (b + r) % 2 == 0: return d
    return None

def chinese_remainder_theorem(remainders, moduli):
    """Teorema del Resto Chino (CRT). Útil para ataques de difusión (Hastad)."""
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    total = 0
    prod = reduce(lambda acc, x: acc * x, moduli)
    for m_i, a_i in zip(moduli, remainders):
        p = prod // m_i
        total += a_i * mul_inv(p, m_i) * p
    return total % prod

def rsa_common_exponent_attack(c1, c2, e1, e2, n):
    """Ataque de Exponente Común si el mismo mensaje se cifra con dos 'e' diferentes."""
    g, s1, s2 = xgcd(e1, e2)
    if s1 < 0:
        c1 = inverse(c1, n)
        s1 = -s1
    if s2 < 0:
        c2 = inverse(c2, n)
        s2 = -s2
    return (pow(c1, s1, n) * pow(c2, s2, n)) % n

def xgcd(a, b):
    """Algoritmo de Euclides extendido auxiliar."""
    if a == 0: return b, 0, 1
    g, x1, y1 = xgcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def xor_brute_force(ciphertext, known_plaintext=b""):
    """Fuerza bruta de 1 byte para encontrar flags en XOR."""
    for k in range(256):
        dec = bytes([b ^ k for b in ciphertext])
        if known_plaintext in dec: return {"key": k, "plaintext": dec}
    return None

def aes_cbc_dec(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(ciphertext)
    return dec[:-dec[-1]] # Auto unpad PKCS7
