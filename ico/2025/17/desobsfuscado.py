import base64
import gzip
import secrets
import string


def codificar_ascii(text):
    return text.encode("ascii")


def comprimir_gzip(text):
    return gzip.compress(text)


def decodificar_ascii(text):
    return text.decode("ascii")


def codificar_base64(text):
    return base64.b64encode(text)


def generar_ruido(ruido):
    text = "x + 2 - 2 + 32 - 64 + 128 + 256"
    ran = secrets.choice(string.ascii_letters)
    eval(text)
    return text, ran


def ofuscar_y_comprimir(texto):
    textoascii = codificar_ascii(texto)
    textob64 = codificar_base64(textoascii)
    b64 = decodificar_ascii(textob64)
    for c in range(32):
        b64 += generar_ruido(c)[1]
    b64 = codificar_ascii(b64)
    return comprimir_gzip(b64)


def guardar_archivo(contenido_bytes):
    archivo_salida = open("output.txt", "wb")
    archivo_salida.write(contenido_bytes)
    archivo_salida.close()


def leer_y_mezclar_bloques():
    archivo_entrada = open("somefile", "rb")
    datos_archivo = archivo_entrada.read()
    bloques_mezclados = bytearray()
    for i in range(0, len(datos_archivo), 32):
        mitad_izquierda = datos_archivo[i :  i+16]
        mitad_derecha = datos_archivo[i+16 : i+32]
        if len(mitad_izquierda) < 16:
            mitad_izquierda += b" " * (16-len(mitad_izquierda))
        if len(mitad_derecha) < 16:
            mitad_derecha += b" " * (16-len(mitad_derecha))
        bloque_invertido = mitad_derecha + mitad_izquierda
        bloques_mezclados.extend(bloque_invertido)
    archivo_entrada.close()
    return bloques_mezclados.decode(encoding="ascii")


guardar_archivo(ofuscar_y_comprimir(leer_y_mezclar_bloques()))
