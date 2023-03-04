import requests
from login import login
from request_parse import RequestParser

def multiple_request(datas: list, url: str, headers):
    for data in datas:
        requests.post(url=url, data=data, headers=headers)


user = {
    "email": "user@itsexpo.com",
    "password": "ITSExpo@2023"
}

url = 'http://127.0.0.1:8000/api/login_user'

bearer_token = login(url, user)["data"]["token"]

field = [{
    "name": "name",
    "type": "Full Name"
}, {
    "name": "yearsEmployed",
    "type": "Number",
    "min": 1,
    "max": 30,
    "decimals": 0
}, {
    "name": "department",
    "type": "Custom List",
    "values": ["R+D", "Marketing", "HR"]
}, {
    "name": "dob",
    "type": "Datetime",
    "min": "1/1/1950",
    "max": "1/1/2000",
    "format": "%m/%d/%Y"
}]   

field = [
    {
        "name": "name",
        "type": "Full Name"
    }
]
req = RequestParser(field, "514a2b80")
multiple_request(req.generate_data(count=10), "127.0.0.1:8000/api/roles", bearer_token=bearer_token)