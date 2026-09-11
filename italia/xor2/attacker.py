def xor_single_byte(data, key):
    return bytes([b ^ key for b in data])

ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")

for i in range(256):
    res = xor_single_byte(ciphertext, i)
    try:
        plaintext = res.decode("utf-8")
        if plaintext.isprintable():
            print(f"Clave {i} (hex {hex(i)}): {plaintext}")
    except:
        pass
