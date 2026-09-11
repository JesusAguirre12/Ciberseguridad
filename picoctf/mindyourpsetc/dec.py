# Tus datos originales
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e = 65537

# Tus factores encontrados
p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477

# Cálculo de la clave privada (d)
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

# Desencriptación
m = pow(c, d, n)

# Conversión a texto
mensaje = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

print(f"El mensaje oculto es: {mensaje}")
