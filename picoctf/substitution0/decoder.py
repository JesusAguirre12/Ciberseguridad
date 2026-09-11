message="ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}"
key="ZGSOCXPQUYHMILERVTBWNAFJDK"
tru="ABCDEFGHIJKLMNOPQRSTUVWXY"
for c in message:
    pos=key.find(c.upper())
    if(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz"):
        print(c,end="")
        continue
    if(c.isupper()):
        print(tru[pos],end="")
        continue
    print(tru[pos].lower(),end="")
