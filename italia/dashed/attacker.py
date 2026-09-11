s=""
with open("decodedusingspaceaswordseparators.txt","r") as f:
    for linea in f:
        s+=linea.strip()

s=s.replace("X","x")
print(s)
