try:
    num=int(input("Enter a number: "))
    print(num*4)
except KeyboardInterrupt:
    print("Number should be entered")
except ValueError:
    print("Please enter a valid number")
print("Bye")