import requests

r = requests.get("https://raw.githubusercontent.com/xinyuchen98/404labs/main/getgoogle.py")
print(r.text)