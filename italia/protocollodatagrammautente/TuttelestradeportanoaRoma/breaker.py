flag="cixd{xsb_zxbpxo_jlofqrof_qb_pxirqxkq}"
abc="abcdefghijklmnopqrstuvwxyz"
for el in flag:
    if el in abc:
       print(abc[(abc.find(el)+3)%26],end="")
    else:
        print(el,end="")
