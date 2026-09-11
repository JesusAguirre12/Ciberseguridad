from Crypto.Cipher import AES

key = b'ICO-NCL202520201'

nonce = b'\x19\xe0\xdb\xf5\xf3\xcb\xe0\xc3 \x82\x90\x01\x83F\x03='

ciphertext = b'b;U\x0cz\x01_|"1\x0cZ\r[\xb4\xd8\x17\x84'

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)

print(repr(plaintext))
print(plaintext.hex())
