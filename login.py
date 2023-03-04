import requests
import json

def find_token(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "token":
                return value
            else:
                token = find_token(value)
                if token is not None:
                    return token
    elif isinstance(data, list):
        for item in data:
            token = find_token(item)
            if token is not None:
                return token
    return None

def login(login_url: str, request):
    res = requests.post(login_url, data=request)
    return json.loads(res.content)

def multiple_request(datas: list, url: str, headers):
    for data in datas:
        requests.post(url=url, data=data, headers=headers)

headers = {
    "Authorization": f"Bearer"
}
