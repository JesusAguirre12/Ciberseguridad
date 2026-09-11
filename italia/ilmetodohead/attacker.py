import requests

url="http://web-07.challs.olicyber.it/"

res=requests.head(url)

print(res.headers)
