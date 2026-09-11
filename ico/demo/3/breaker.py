from base64 import b64decode, b64encode
from hashlib import md5
from Cryptodome.Hash import Poly1305

USERNAME_TOKEN_SIZE = 30
UUID_TOKEN_SIZE = 36
P = (1 << 130) - 5


def toi(b): #bytes
    return int.from_bytes(b, "little")


def tob(x): #int
    return x.to_bytes(16, "little")


def parse(token): #str
    raw = b64decode(token)
    nonce = raw[:16]
    data = raw[16:16+USERNAME_TOKEN_SIZE+UUID_TOKEN_SIZE]
    tag = raw[16+USERNAME_TOKEN_SIZE+UUID_TOKEN_SIZE:]
    return nonce,data,tag


def recover(token): #str
    nonce, data, tag = parse(token)

    m = toi(md5(data).digest())+(1<<128)
    s = toi(nonce)
    t = toi(tag)
    base=(t-s)%(1<<128)
    inv_m=pow(m,-1,P)
    for k in range(4):
        acc=base+(1<<128)*k
        r= (acc*inv_m)%P
        if r>=(1<<128):
            continue
        rb=tob(r)
        test = Poly1305.Poly1305_MAC(rb, nonce, md5(data).digest()).digest()
        if test == tag:
            return rb

    raise ValueError("ocurrió un problema")

#bytes, str, str, bytes
def solve(rb, username, uuid_str, nonce):
    if isinstance(username, str):
        username = username.encode()
    if isinstance(uuid_str, str):
        uuid_str = uuid_str.encode()

    if len(uuid_str) != UUID_TOKEN_SIZE:
        raise ValueError("uuid inválido: debe medir 36 bytes")

    data = username[:USERNAME_TOKEN_SIZE].ljust(USERNAME_TOKEN_SIZE, b"\x00") + uuid_str
    hashed = md5(data).digest()
    tag = Poly1305.Poly1305_MAC(rb, nonce, hashed).digest()
    return b64encode(nonce + data + tag).decode()

#bytes
def print_key(rb):
    print("r hex   :", rb.hex())
    print("r bytes :", rb)
    print("r normal:", rb.decode("latin-1"))


user = "flag3_user"
pas = "df3174be-2b0f-4ee3-8507-2156a347df88"


token_valido = "SmAw5jiSU8QpjuefxxCNoWFkbWluaXN0cmF0b3IAAAAAAAAAAAAAAAAAAAAAADIyYzU2NzkzLWYyYTgtNDk0NC04OTc5LTM2ZjYxNTc3ZDZjOCa3kY5DkWB8+0i/Xl34dUo="

r = recover(token_valido)
print_key(r)
nuevo = solve(r,username=user,uuid_str=pas,nonce=b"\x00" * 16)

print("\nToken nuevo:")
print(nuevo)
