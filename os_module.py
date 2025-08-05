import os
folder = input("Enter the folder name: ")
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created successfully.")
else:
    print("Folder already exists.")