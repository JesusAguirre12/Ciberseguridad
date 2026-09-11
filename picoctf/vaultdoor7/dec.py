x = [1]*8

x[0] = 1096770097
x[1] = 1952395366
x[2] = 1600270708
x[3] = 1601398833
x[4] = 1716808014
x[5] = 1734305378
x[6] = 825374004
x[7] = 912340068

ans = []

for i in range(0,8):
    c1=x[i]>>24
    c2=(x[i]^(c1<<24))>>16
    c3=(x[i]^((c1<<24)|(c2<<16)))>>8
    c4=(x[i]^((c1<<24)|(c2<<16)|(c3<<8)))
    ans.append(c1)
    ans.append(c2)
    ans.append(c3)
    ans.append(c4)

print(f"picoctf{{{"".join(chr(i) for i in ans)}}}")
