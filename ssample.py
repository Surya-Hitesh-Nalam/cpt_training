num=int(input("Enter a number: "))
deno=int(input("Enter a denominator: "))
try:
    result = num / deno
    print(f"The result of {num} divided by {deno} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")