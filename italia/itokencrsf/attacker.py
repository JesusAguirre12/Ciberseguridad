import requests

url1 = "http://web-11.challs.olicyber.it/login"
url2 = "http://web-11.challs.olicyber.it/flag_piece"
session = requests.Session()

res = session.post(url1, json={"username": "admin", "password": "admin"})
data = res.json()
csrf = data["csrf"]

flag = ""

for i in range(4):
    cont = session.get(url2, params={"index": i, "csrf": csrf})
    res_data = cont.json()
    print(f"Respuesta {i}:", res_data)
    for key in ["flag","fl4g","flag_piece"]:
        if key in res_data:
            flag += str(res_data[key])
            break
    if "csrf" in res_data:
        csrf = res_data["csrf"]

print(f"\nFlag completa: {flag}")
