from itertools import cycle
import base64

ciphertext = "ATeoQFBajaDgn2DytcSccrJaqW4rQFUMQKJeR3AtdRpyBKQfYPkuBiM7Y0OmQYlmuMPaZI0="

# 1. Definimos tus dos alfabetos y tus dos claves
a1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a2 = "abcdefghijklmnopqrstuvwxyz"

k1 = "INTERNATIONAL"
k2 = "international"

ks = cycle(range(len(k1)))

out = []

for c in ciphertext:
    if c.isupper():
        shift = a1.index(k1[next(ks)])
        ni = (a1.index(c) - shift) % 26
        out.append(a1[ni])
        
    elif c.islower():
        shift = a2.index(k2[next(ks)])
        ni = (a2.index(c) - shift) % 26
        out.append(a2[ni])
        
    else:
        out.append(c)

print(base64.b64decode("".join(out)).decode('latin1'))
