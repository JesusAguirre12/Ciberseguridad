import requests

url = "http://web-10.challs.olicyber.it/"

# Consultar los métodos permitidos
res_options = requests.options(url)
print("Métodos permitidos (Allow):", res_options.headers.get("Allow"))
