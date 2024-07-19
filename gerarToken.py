import requests

url = 'https://api.rd.services/auth/token?token_by=code'
headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}
data = {
    "client_id": "c61915f1-7e66-4d2e-a4e1-df53c0b1c003",
    "client_secret": "2b587f2eace64f909be625809b03f235",
    "code": "e3d04c56e1bae31ba141c99767377ab1"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
