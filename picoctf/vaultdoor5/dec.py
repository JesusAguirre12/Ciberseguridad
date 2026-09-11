import base64 as b64
import urllib.parse #se puede tambien con esta

# .quote     encripta
# .unquote   desencripta

texto = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM3JTY2JTM4JTM1JTM1JTY2JTYzJTM1"
texto = b64.b64decode(texto)

texto = texto.decode('utf-8') 

flag = ""

for i in range(1,len(texto),3):
    flag += chr(int(texto[i:i+2], 16))  

print(f"picoCTF{{{flag}}}")
