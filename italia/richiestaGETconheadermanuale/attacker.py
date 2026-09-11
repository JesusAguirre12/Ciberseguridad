import requests

url = "http://web-03.challs.olicyber.it/flag"
headers = {
    "X-Password": "admin"
}
response = requests.get(url, headers=headers)

print(response.text)
