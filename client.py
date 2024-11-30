import requests 

url = "http://localhost:8000/items/1234?category=cat1&dept=12"
body = {"pers": {
    "name":"name1","id":"12", "mobiles": ["iphone", "nokia"]
    },
"extra_body": "1234"

}
resp = requests.post(url, json=body)
print(resp)