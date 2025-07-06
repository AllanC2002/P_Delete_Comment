import requests

BASE_URL = "http://52.204.34.56:8080/delete-comment"

login_data = {
    "User_mail": "allan",  
    "password": "1234"
}

login_response = requests.post("http://52.203.72.116:8080/login", json=login_data)
if login_response.status_code != 200:
    print("Login error:", login_response.status_code, login_response.text)
    exit()

token = login_response.json()["token"]
print("Token:", token)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

comment_id = "68687b0aa0485df1e4a1ee14"  

payload = {
    "comment_id": comment_id
}

response = requests.put(BASE_URL, json=payload, headers=headers)

print("Status:", response.status_code)
try:
    print("Response:", response.json())
except Exception as e:
    print("No json:", response.text)
