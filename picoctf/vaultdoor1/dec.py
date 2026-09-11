text = "password.charAt(0)  == 'd' && password.charAt(29) == '2' && password.charAt(1)  == '3' && password.charAt(4)  == 'r' && password.charAt(2)  == '5' && password.charAt(23) == 'r' && password.charAt(3)  == 'c' && password.charAt(17) == '4' && password.charAt(1)  == '3' && password.charAt(7)  == 'b' && password.charAt(10) == '_' && password.charAt(5)  == '4' && password.charAt(9)  == '3' && password.charAt(11) == 't' && password.charAt(15) == 'c' && password.charAt(8)  == 'l' && password.charAt(12) == 'H' && password.charAt(20) == 'c' && password.charAt(14) == '_' && password.charAt(6)  == 'm' && password.charAt(24) == '5' && password.charAt(18) == 'r' && password.charAt(13) == '3' && password.charAt(19) == '4' && password.charAt(21) == 'T' && password.charAt(16) == 'H' && password.charAt(27) == 'e' && password.charAt(30) == '6' && password.charAt(25) == '_' && password.charAt(22) == '3' && password.charAt(28) == 'f' && password.charAt(26) == '1' && password.charAt(31) == '6'"

ls = text.split(" && ")
flag = ["_"]*32

print(ls)

for el in ls:
    idx1 = el[16]
    idx2 = el[17]
    if(idx2 != ')'):
        idx1+=idx2
    print(int(idx1))
    flag[int(idx1)]=el[-2]
   
print(f"picoCTF{{{''.join(flag)}}}")


