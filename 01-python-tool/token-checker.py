import requests

def check_token(api_url, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
