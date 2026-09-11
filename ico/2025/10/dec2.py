cipher = b"w).%v0}YMR9!J;%k4mZ='*'1Jz7q9&'s373P"
key = b"1L\\f&c|cu|"[::-1]

print(bytes(cipher[i]^key[i%len(key)] for i in range(len(cipher))))
