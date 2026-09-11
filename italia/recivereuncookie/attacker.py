import requests

url="http://web-06.challs.olicyber.it/token"

session=requests.Session()
#hacer la primera petición para recibir e instalar la cookie de sesión
session.get("http://web-06.challs.olicyber.it/token")
#aca hacemos la peticion con la cookie de sesion que ya tenemos
req=session.get("http://web-06.challs.olicyber.it/flag")

print(req.text)
