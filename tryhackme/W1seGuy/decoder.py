s = "337b1d4a1556523c5f11224b2470111307335a06265d2202040b7f2959301547290110154b1f4318"
flag = "THM{"

nueva = bytes.fromhex(s)

print("flagdecodeada: ", nueva)

print("acalaflag: ")
for i in range(len(flag)):
	print(chr(ord(flag[i])^nueva[i]),end="")
