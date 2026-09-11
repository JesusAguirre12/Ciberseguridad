import requests

url = "http://web-10.challs.olicyber.it/"

# Al hacer la petición a los métodos que devolvieron 500
res = requests.put(url)

print("Status Code:", res.status_code)
print("Cuerpo de la respuesta:")
print(res.text)  # Aquí debería aparecer el mensaje de error o la flag
