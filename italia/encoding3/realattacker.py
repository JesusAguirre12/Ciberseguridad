from Cryptodome.Util.number import long_to_bytes
from base64 import b64decode

dec = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")
num = 664813035583918006462745898431981286737635929725

# Convierte el número a bytes automáticamente sin pedir tamaño
num_bytes = long_to_bytes(num) 

print((dec + num_bytes).decode())
