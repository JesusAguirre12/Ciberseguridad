s="synt{CAESAR_ME!-l0h_T07_vG_e1tuG!}"
abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for el in s:
    if el in abc:
        pos=abc.find(el)
        np=(pos+26-13)%26
        if el.isupper():
            np+=26
        print(abc[np],end="")
    else: 
        print(el,end="")
