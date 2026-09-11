import requests
url = "http://too-small-reminder.challs.olicyber.it"
session = requests.Session()
payload = {
    'username': 'pepeasd1as',
    'password': '123'
}
reg = session.post(f"{url}/register",json=payload)
print("Registro:", reg.text)

login = session.post(f"{url}/login", json=payload)
print("Login:", login.text)

cookies = session.cookies.get_dict()
print("Cookies de sesión:", cookies)

res_admin = session.get(f"{url}/admin")
print("Respuesta Admin:", res_admin.text)
