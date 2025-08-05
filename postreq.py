import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "HI",
    "body": "hari",
    "userId": 1
}
res=requests.post(url, json=data)
print("Status Code:", res.status_code)
print("Response JSON:", res.json())