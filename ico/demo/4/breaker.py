from base64 import b64decode, b64encode
from hashlib import md5
from Cryptodome.Hash import Poly1305
from Crypto.Util.Padding import pad
import hashlib

#byte byte
def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

#str str bytes

def recoverp(name, desc, pas):
    fn = pad(name.encode(),8)[:8]
    hashed = hashlib.md5(desc.encode()).digest()
    mp=len(pas)%4
    if mp:
        pas+='='*(4-mp)
    
    pas = b64decode(pas)
    pb = xor_bytes(xor_bytes(pas, fn), hashed)
    return pb

#str str str
def solve(name, desc, passs):
    fn = pad(name.encode(), 8)[:8]
    hashed_desc = hashlib.md5(desc.encode()).digest()
    resultado_xor = xor_bytes(xor_bytes(passs, fn), hashed_desc)
    p = b64encode(resultado_xor).decode().strip('=')
    
    return p

#datos de la nota

dd="asaasdfasdfsdf"
name="asdfasdfasdf"
pas=b"Fc6+9FOTA8I="

passs=recoverp(name,dd,pas)
print(solve('Note for flag 4', 'This is a note for flag 4', passs))
