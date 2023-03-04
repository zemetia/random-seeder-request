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

from login import login, find_token, multiple_request,headers
from request_parse import RequestParser

user = {
    "email": "user@itsexpo.com",
    "password": "ITSExpo@2023"
}

login_res = login('http://127.0.0.1:8000/api/login_user', user)
bearer_token = find_token(login_res)
headers["Authorization"] = f"Bearer {bearer_token}"
req = RequestParser(field, "514a2b80")
res = req.generate_data(count=10)
multiple_request(res, '', headers)

