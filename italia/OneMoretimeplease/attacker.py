import string

def es_caracter_valido(byte_val):
    return chr(byte_val) in string.printable and byte_val not in (11, 12)

def romper_many_time_pad(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        lineas_hex = [linea.strip() for linea in f if linea.strip()]
    mensajes = [bytes.fromhex(h) for h in lineas_hex]
    max_len = max(len(m) for m in mensajes)
    clave_recuperada = bytearray()
    # 2. Iterar posición por posición (columna por columna)
    for i in range(max_len):
        mejor_candidato_k = 0
        max_validos = -1

        # Probar todas las posibles claves de 1 byte (0 a 255)
        for k in range(256):
            coincidencias = 0
            
            # Probar el candidato 'k' contra la posición 'i' de cada mensaje
            for msg in mensajes:
                if i < len(msg): # Asegurar que el mensaje tenga bytes en esta posición
                    decrypted_byte = msg[i] ^ k
                    if es_caracter_valido(decrypted_byte):
                        coincidencias += 1
                        # Ponderación extra si es una letra, espacio o número común
                        if chr(decrypted_byte) in string.ascii_letters + ' ':
                            coincidencias += 0.5
            
            # Guardar el candidato con la mayor puntuación
            if coincidencias > max_validos:
                max_validos = coincidencias
                mejor_candidato_k = k

        clave_recuperada.append(mejor_candidato_k)

    # 3. Imprimir los resultados descifrados con la clave encontrada
    print(f"=== CLAVE RECUPERADA (HEX): {clave_recuperada.hex()} ===\n")
    print("=== MENSAJES DESCIFRADOS ===")
    
    for idx, msg in enumerate(mensajes):
        # Aplicar XOR de cada mensaje con la clave recuperada
        plaintext_bytes = bytes([b ^ k for b, k in zip(msg, clave_recuperada)])
        # Decodificar reemplazando caracteres desconocidos si los hubiera
        plaintext = plaintext_bytes.decode('utf-8', errors='replace')
        print(f"Msg {idx + 1}: {plaintext}")

if __name__ == "__main__":
    # Cambia 'output.txt' por la ruta de tu archivo
    romper_many_time_pad('output.txt')
