ls = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
"0x55", "0x6e", "0x43", "0x68", "0x5f", "0x30", "0x66", "0x5f",
"142", "131", "164", "63" , "163", "137", "40" , "063" ,
'0' , 'd' , 'c' , '8' , '5' , 'b' , 'e' , 'd' ,]

flag=""

#ascii
#hex
#oct
#chr
#chr(0o142)
#chr(0x55) de haber sabido esto antes mejor
for i in range(8):
    flag+=chr(ls[i])

for i in range(8,16):
    flag+=chr(int(ls[i],16))
    
for i in range(16,24):
    flag+=chr(int(ls[i],8))

for i in range(24,32):
    flag+=ls[i]

print(f"picoCTF{{{flag}}}")
