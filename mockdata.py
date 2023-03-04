import requests
import json
import ast

class MockData:
    def __init__(self, fields, key: str, url:str, method: str):
        self.headers = {}
        self.fields = fields
        self.key = key
        self.url = url
        self.method = method.lower()

    def append_headers(self, headers):
        self.headers.update(headers)

    def find_token(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "token":
                    return value
                else:
                    token = MockData.find_token(value)
                    if token is not None:
                        return token
        elif isinstance(data, list):
            for item in data:
                token = MockData.find_token(item)
                if token is not None:
                    return token
        return None
    
    def login(self, login_url: str, request):
        res = requests.post(login_url, data=request)
        bearer_token = MockData.find_token(json.loads(res.content))
        if bearer_token != None:
            print("Successfully got the bearer token!")
            self.headers["Authorization"] = f"Bearer {bearer_token}"
        else: print("There is no bearer token found! try again.")

    def generate_data(self, count=100):
        data = {
            "key": self.key,
            "count": count,
            "fields": json.dumps(self.fields)
        }
        res = requests.get("https://api.mockaroo.com/api/generate.json", params=data)
        return json.loads(res.content)

    def send_request(self, datas):
        for data in datas:
            requests.request(method=self.method, url=self.url, data=data, headers=self.headers)

    def generate_request(self, count=100):
        self.send_request(self.generate_data(count))

    def parse_string(string):
        try:
            return ast.literal_eval(string)
        except (ValueError, SyntaxError):
            return string

    def parse_field(field):
        decode_field = []
        temp = {}
        for a, b in enumerate(field.items()):
            temp = {}
            temp["name"] = b[0]
            for i in b[1].split("|"):
                x = i.split(":")
                temp[x[0]] = MockData.parse_string(x[1])
            decode_field.append(temp)
        return decode_field