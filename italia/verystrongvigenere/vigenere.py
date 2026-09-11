encod = "fzau{ncn_isors_cviovw_pwcqoze}"
clave = "AOAOAOAOAOAOAOAOAOAOAOAOAOAOAO"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def descifrar_vigenere(texto, clave):
    resultado = []
    j = 0
    for char in texto:
        if char.upper() in ABC:
            es_mayus = char.isupper()
            c_idx = ABC.index(char.upper())
            k_char = clave[j % len(clave)].upper()
            k_idx = ABC.index(k_char)
            p_idx = (c_idx - k_idx) % 26
            char_descifrado = ABC[p_idx]
            resultado.append(char_descifrado if es_mayus else char_descifrado.lower())
            j += 1
        else:
            resultado.append(char)
    return "".join(resultado)
flag = descifrar_vigenere(encod, clave)
print(f"Flag: {flag}")
