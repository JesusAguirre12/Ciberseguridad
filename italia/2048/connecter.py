import socket
import sys
import time

sys.set_int_max_str_digits(0)

# Socket directo a nivel de OS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect(("2048.challs.olicyber.it", 10007))

# Mapeo directo para evitar el overhead de `.index()` o `if/elif`
OPS = {
    b"SOMMA": lambda a, b: a + b,
    b"PRODOTTO": lambda a, b: a * b,
    b"DIFFERENZA": lambda a, b: a - b,
    b"POTENZA": lambda a, b: pow(a, b),
    b"DIVISIONE_INTERA": lambda a, b: a // b,
}

# Descartar banner inicial de bienvenida
s.recv(1024)

start = time.time()

for i in range(2048):
    buf = b""
    while buf.count(b" ") < 2:
        chunk = s.recv(256)
        if not chunk:
            break
        buf += chunk

    # Parseo directo sobre bytes
    partes = buf.strip().split()
    op, a, b = partes[0], int(partes[1]), int(partes[2])

    res = OPS[op](a, b)
    s.sendall(str(res).encode() + b"\n")

    if (i + 1) % 1 == 0:
        print(f"Iteración {i + 1}/2048 - Tiempo: {time.time() - start:.2f}s")

print(f"\n¡Completado en {time.time() - start:.2f}s!")
print(s.recv(1024).decode())
s.close()