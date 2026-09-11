import os 
import math 

innodes = []
for i in range(12,25):
    innodes.append(str(i))
    
for node in innodes:
    res = os.popen(f'icat -o 2048 disk.flag.img {node} | strings | grep -Ei "picoCTF{{.*?}}"').read()
    print(res) 
