cipher = b"w).%v0}YMR9!J;%k4mZ='*'1Jz7q9&'s373P"
key = b"1L\\f&c|cu|"

for shift in range(len(key)):
    p = bytes(cipher[i]^key[(i+shift)%len(key)] for i in range(len(cipher)))
    print(shift, p)
