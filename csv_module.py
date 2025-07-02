import csv 
with open("people.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    for _ in range(2):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        writer.writerow([name,age])
print("Data written to people.csv")