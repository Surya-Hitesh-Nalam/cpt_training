import json
name=input("Enter your name: ")
age=int(input("Enter your age: "))

data = {
    "name": name,
    "age": age
}

stringify_json = json.dumps(data)
print("JSON String:", stringify_json)

with open("user.json","w") as f:
    json.dump(data,f)

print("Data written to json folder")

with open("user.json","r") as f:
    data_read= json.load(f)
    print("Data read from json file:",data_read)