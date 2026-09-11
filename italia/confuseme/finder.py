import hashlib
i = 0
while True:
    candidate = f"0e{i}"
    md5_hash = hashlib.md5(candidate.encode()).hexdigest()[:24]
    if md5_hash.startswith("0e") and md5_hash[2:].isdigit():
        print(f"[!] Valor encontrado: {candidate}")
        print(f"[!] Hash (primeros 24 chars): {md5_hash}")
        break
    i += 1
