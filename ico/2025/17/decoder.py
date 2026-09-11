import base64
import gzip


def descompresor_y_desofuscar():
    with open("output.txt", "rb") as f:
        contenido_comprimido = f.read()

    datos_b64_con_ruido = gzip.decompress(contenido_comprimido).decode("ascii")
    datos_b64 = datos_b64_con_ruido[:-32]
    texto_mezclado_bytes = base64.b64decode(datos_b64)

    return texto_mezclado_bytes


def desmezclar_bloques(datos_mezclados):
    bloques_originales = bytearray()

    for i in range(0, len(datos_mezclados), 32):
        bloque = datos_mezclados[i : i + 32]
        mitad_derecha_orig = bloque[0:16]
        mitad_izquierda_orig = bloque[16:32]
        bloques_originales.extend(mitad_izquierda_orig + mitad_derecha_orig)
    return bloques_originales.decode("ascii").rstrip()


# --- EJECUCIÓN DEL PROCESO INVERSO ---
texto_mezclado = descompresor_y_desofuscar()
texto_original = desmezclar_bloques(texto_mezclado)

print("texto recuperado")
print(texto_original)
