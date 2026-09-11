import requests 

url="http://web-01.challs.olicyber.it/"
res=requests.get(url)
print(res.text)
