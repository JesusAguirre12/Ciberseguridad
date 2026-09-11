import requests

url = "http://web-02.challs.olicyber.it/server-records"
parametros = {"id": "flag"}  

"""
mas parametros se puede hacer asi

{
    "id":"flag",
    "user":"admin",
    ...
}
"""
response = requests.get(url, params=parametros)
print(response.text)
