import pandas as pd

print("Enter 4 random numbers , sapce seperated")
numbers = input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers)!=4:
        raise ValueError('please provide exactly 4 numbers')
    total_data= pd.Series(numbers)
    print(total_data)

    filtered_data = total_data[total_data>10]
    print("values>10")
    print(filtered_data)
except ValueError as e:
    print(e)
