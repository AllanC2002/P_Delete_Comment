import requests

BASE_URL = "http://localhost:8081/delete-comment"

login_data = {
    "User_mail": "ascorread1",  
    "password": "1234"
}

login_response = requests.post("http://localhost:8080/login", json=login_data)
if login_response.status_code != 200:
    print("Login error:", login_response.status_code, login_response.text)
    exit()

token = login_response.json()["token"]
print("Token:", token)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

comment_id = "685772c09d450317d6b0ec4b"  

payload = {
    "comment_id": comment_id
}

response = requests.put(BASE_URL, json=payload, headers=headers)

print("Status:", response.status_code)
try:
    print("Response:", response.json())
except Exception as e:
    print("No json:", response.text)
