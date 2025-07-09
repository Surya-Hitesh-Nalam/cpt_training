with open('file1.txt', 'r+') as fileobj:
    content = fileobj.read()
    fileobj.seek(10)
    fileobj.write("Modification done here")