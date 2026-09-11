import hashlib
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_{}0123456789"
with open("ct.txt", "r") as f:
    for linea in f:
        s=linea.strip()
        for c in chars:
            if(hashlib.sha256(c.encode()).hexdigest()==s):
                print(c,end="")
                break
