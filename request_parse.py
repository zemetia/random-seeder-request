# https://www.mockaroo.com/docs
import requests
import json

class RequestParser:
    def __init__(self, fields, key: str):
        self.fields = fields
        self.key = key
    
    def generate_data(self, count=100):
        data = {
            "key": self.key,
            "count": count,
            "fields": json.dumps(self.fields)
        }
        res = requests.get("https://api.mockaroo.com/api/generate.json", params=data)
        return json.loads(res.content)


            