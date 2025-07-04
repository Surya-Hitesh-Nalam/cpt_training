try:
    file = open("people.csv")
    str=file.readlines()
    for line in str:
        print(line.strip())
except IOError as e:
    print("Error occured during input take ...")
else:
    print("File read successfully")