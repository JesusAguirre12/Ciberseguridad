s=""
with open("obtained.txt", "r") as f:
    s="".join(l.strip() for l in f)

s2=""
for i in range(0,len(s),8):
    cnt=0
    for j in range(i+7,i-1,-1):
         cnt+=(1<<(7-j+i))*int(s[j])
    print(chr(cnt),end="")
