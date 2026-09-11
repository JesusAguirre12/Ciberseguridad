def switchBits(c,p1,p2):
    c1=(c>>p1)&1
    c2=(c>>p2)&1
    if(c1==c2):
        return c
    c^=(1<<p1 | 1<<p2)
    return c
    
arr=[0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC1, 0xC0, 0x95, 0x94, 0x94, 0xC1, 0xD1, 0xE1, 0xF1]

"""
c = switchBits(c,1,2); 
c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ 
c = switchBits(c,5,6); 
c = switchBits(c,4,7);
c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ 
c = switchBits(c,3,4); 
c = switchBits(c,2,5); 
c = switchBits(c,6,7); 
"""

def op(el):
    c = el
    c = switchBits(c,6,7)
    c = switchBits(c,2,5)
    c = switchBits(c,3,4)
    c = switchBits(c,0,1)
    c = switchBits(c,4,7)
    c = switchBits(c,5,6)
    c = switchBits(c,0,3)
    c = switchBits(c,1,2)
    return c

print(f"picoCTF{{{"".join(chr(op(el)) for el in arr)}}}")
