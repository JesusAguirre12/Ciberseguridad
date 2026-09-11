import requests

# 1. Definir la URL de destino
url = "http://web-08.challs.olicyber.it/login"

# 2. Definir los datos del formulario en un diccionario
datos = {
    "username": "admin",
    "password": "admin"
}

# 3. Realizar la petición POST pasando los datos mediante la palabra clave 'data'
response = requests.post(url, data=datos)

# 4. Mostrar la respuesta devuelta por el servidor
print("Código de estado:", response.status_code)
print("Respuesta:")
print(response.text)
