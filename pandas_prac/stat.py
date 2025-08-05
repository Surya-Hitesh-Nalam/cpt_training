import pandas as pd

print("Enter 5 random numbers , space seperated")
numbers = input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers)!=5:
        raise ValueError('please provide exactly 5 numbers')
    series = pd.Series(numbers,index=['a', 'b', 'c', 'd', 'e'])
    print(series)
#statistics
    print("\n Statistics:")
    print("Mean:", series.mean())
    print("Median:", series.median())
    print(f"Sum:", series.sum())
    print("Standard Deviation:", series.std())
    print("Variance:", series.var())
    print("Minimum:", series.min())
    print("Maximum:", series.max())
#Attributes
    print("\n Attributes:")
    print("Data Type:", series.dtype)
    print("Index:", {series.index}.tolist())
    print("Values:", {series.values}.tolist())
    print("Size:", series.size)
    print("Shape:", series.shape)
except ValueError as e:
    print(e)
