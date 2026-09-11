cipher = b"w).%v0}YMR9!J;%k4mZ='*'1Jz7q9&'s373P"
key = b"1L\\f&c|cu|"

cip=cipher.hex()

plain = bytes(
    cipher[i] ^ key[i % len(key)]
    for i in range(len(cipher))
)

print(plain)
print(plain.decode(errors="replace"))
print(cip)
