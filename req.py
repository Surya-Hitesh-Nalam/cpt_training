import requests
res=requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(res.status_code)
print(res.json())