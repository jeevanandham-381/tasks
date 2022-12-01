import requests

val = input("which is do you want")
response = requests.get(f"http://localhost:1111n/{val}")
print(response.json())
print(response.status_code)
