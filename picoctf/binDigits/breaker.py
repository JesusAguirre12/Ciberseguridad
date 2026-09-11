data = bytearray()

with open("digits.bin", "r") as archivo:
    bits = archivo.read().replace("\n", "").replace(" ", "").strip()
    
    for i in range(0, len(bits), 8):
        byte_str = bits[i:i+8]
        if len(byte_str) == 8:
            data.append(int(byte_str, 2))

with open("resultado.jpeg", "wb") as f:
    f.write(data)

print("¡Archivo 'resultado.jpeg' generado con éxito!")
