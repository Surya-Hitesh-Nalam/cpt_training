with open("file1.txt","a+") as file:
    file.write("This is an appended line.\n")
    file.seek(0)
    content = file.read()
    print(content)  