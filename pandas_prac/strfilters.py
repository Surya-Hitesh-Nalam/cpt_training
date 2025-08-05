'''Code eloborate how to filter string data in series based on a insensitivity '''
import pandas as pd

print("Enter 5 random strings , sapce seperated")
strings = input().strip().split()
print("Enter substring")
substring = input().strip()
try:
    if len(strings)!=5:
        raise ValueError('please provide exactly 5 strings')
    series= pd.Series(strings)
    print("Orginal series:",)
    print(series)
    # using list comprehensions
    filtered_data = series[series.str.lower().str.contains(substring.lower(),na=False)]
    
    print(f"strings containing '{substring}'(case insensitive):")
    print(filtered_data if not filtered_data.empty else "No match found.")
except ValueError as e:
    print(e)
