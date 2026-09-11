key = bytes.fromhex("b230bddc107ae17b2c3be2ec9901")
flag = bytes.fromhex("d45cdcbb6b1ed34a4a5ed2dfac7c")
result = "".join(chr(k ^ f) for k, f in zip(key, flag))
print(result)
