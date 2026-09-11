import requests

url = "http://web-10.challs.olicyber.it/"

headers = {
    "X-Method": "POST"
}

# Realizar una petición POST real en lugar de GET
response = requests.post(url, headers=headers)

print("Código de estado:", response.status_code)
print("Flag en headers:", response.headers) 
#se puede hacer headers.get("nombre del header")
