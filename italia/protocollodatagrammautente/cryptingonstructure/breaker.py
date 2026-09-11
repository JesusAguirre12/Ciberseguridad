#reemplazamos A=0 y B=1 y lo tomamos como el alfabeto de bacon

s="0000100000000100111001101010001001010010011101001100000100101001111000"
ass="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("flag{",end="")
for i in range(0,len(s),5):
    cnt=0
    for j in range(i+4,i-1,-1):
        cnt+=(1<<((5-j+i-1)))*int(s[j])
    print(ass[cnt],end="")
print("}")
