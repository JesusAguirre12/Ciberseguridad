from base64 import b64encode, b64decode
text = "N2IgNGQgMzMgMzUg MzUgNDAgNDcgMzMg NWYgMzEgNmUg NTAgNmMgMzEgMzQg NmUgNWYgMzUgMzEg NjcgNjggMzQgN2Q="

#fijarse en la captura que no corresponde al mensaje es decir, que esta de mas, por ej el i, ni el je, ni el # corresponden al mensaje enviado, para eso se analiza la captura

arr=text.split(" ")
print(arr)
for el in arr: 
    enc = b64decode(el.encode('utf-8'))
    arr=[]
    if(b' ' in enc): 
        arr=enc.split(b' ')
        
    for c in arr:
        r=bytes.fromhex(c.decode('utf-8')).decode('utf-8')
        print(r,end="")
    
