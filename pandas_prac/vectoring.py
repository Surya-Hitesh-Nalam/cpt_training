import pandas as pd
print("Enter 4 numbers separated with space:")
numbers = input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers)!=4:
        raise ValueError('Please provide exactly 4 numbers')
    series = pd.Series(numbers,index=['a', 'b', 'c', 'd'])
    print("\n Original Series:")
    print(series)

    doubled=series*2
    print("\n Series after doubling the values:")
    print(doubled)
    added = series + 100
    print("\n Series after adding 100 to each value:")
    print(added)
    
except ValueError as e:
    print(e)