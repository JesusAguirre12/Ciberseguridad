def descifrar_con_mensaje_conocido(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        lineas_hex = [linea.strip() for linea in f if linea.strip()]
    mensajes = [bytes.fromhex(h) for h in lineas_hex]
    msg1_plano = "IL CRITTOSISTEMA CHE STO UTILIZZANDO SEMBRA INDISTRUTTIBILE"
    msg1_bytes = msg1_plano.encode()
    c1 = mensajes[0]
    clave_real = bytes([b ^ char_b for b, char_b in zip(c1, msg1_bytes)])
    print(f"=== CLAVE REVELADA (HEX) ===")
    print(clave_real.hex())
    print("\n" + "="*40 + "\n")

    print("=== MENSAJES DESCIFRADOS ===")
    for idx, msg in enumerate(mensajes):
        plaintext_bytes = bytes([b ^ k for b, k in zip(msg, clave_real)])
        plaintext = plaintext_bytes.decode('utf-8', errors='replace')
        print(f"Msg {idx + 1}: {plaintext}")

if __name__ == "__main__":
    descifrar_con_mensaje_conocido('output.txt')
