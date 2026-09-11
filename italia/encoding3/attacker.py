from base64 import b64decode

dec = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")
num = 664813035583918006462745898431981286737635929725
num_bytes = num.to_bytes((num.bit_length() + 7) // 8, 'big')
flag = (dec + num_bytes).decode()

print(flag)
