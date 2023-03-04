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

field = {
    "name": "type:Full Name",
    "yearsEmployed": "type:Number|min:1|max:30|decimals:0",
    "department": "type:Custom List|values:['R+D', 'Marketing', 'HR']",
    "dob": "type:Datetime|min:1/1/1950|max:1/1/2000|format:%m/%d/%Y"
}


from mockdata import MockData

user = {
    "email": "<email>",
    "password": "<password>"
}

mock = MockData(MockData.parse_field(field), "<mockaroo api key>", "<api service url to seed>", "post")
mock.login('http://127.0.0.1:8000/api/login_user', user)
mock.generate_request(1000)

