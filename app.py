import requests

link = "http://google.com"
f = requests.get(link)
print(f.text)