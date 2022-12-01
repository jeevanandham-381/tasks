import requests
responce=requests.get("http://localhost:1111")
print(responce.json())
print(responce.status_code)