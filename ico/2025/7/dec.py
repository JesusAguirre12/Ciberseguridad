text = input("Enter a message to encrypt: ")
key = int(input("Enter the key: "))
encrypted_text = []

for ch in text:
    # `ord(ch)` convierte el carácter a su valor ASCII
    # `chr(...)` convierte el valor ASCII de vuelta a carácter
    ch_encrypted = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    encrypted_text.append(ch_encrypted)

result = "".join(encrypted_text)
print(f"Encrypted message: {result}")
