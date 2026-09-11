import base64

# Lista de datos proporcionada
data = [
    "ezF0X3c0cw==O", "I+znCJg=O", "/9QZRtc=O", "uF+2UTs=O", "pDW7rkI=O",
    "8esVOK4=O", "cGljb0NURg==O", "KWEh2jQ=O", "BGAVCe8=O", "RA+7xFw=O",
    "YmhfNHJfZA==O", "CMEx344=O", "PGb6oYA=O", "uSy5rvo=O", "bnRfdGg0dA==O",
    "MTA2NTM4NA==O", "xIJPbWg=O", "XzM0c3lfdA==O", "oDis5T8=O", "v2XglLs=O",
    "fQ==O", "STneebY="
]

def decode_data(items):
    dl = []
    for item in items:
        clean_item = item.rstrip('O')
        missing_padding = len(clean_item) % 4
        if missing_padding:
            clean_item += '=' * (4 - missing_padding)
            
        try:
            decoded_bytes = base64.b64decode(clean_item)
            dl.append(decoded_bytes.decode('utf-8', errors='ignore'))
        except Exception as e:
            dl.append(f"Error decodificando {item}: {e}")
            
    return dl

resultados = decode_data(data)
for res in resultados:
    print(res)
