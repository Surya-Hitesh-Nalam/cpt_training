import pandas as pd
"""
1. series (1D array)
2. DataFrame(2D array)/labeling will be on rows and columns
Operations:
1. Reading/Writing of data (csv/json/xls)
2. Inserting of data
3. Selecting of data
4. Data manupulation
5. Grouping and aggregation
6. merging / joining
7. sorting
"""
print("Enter 3 names seperated with space:")
names= input().strip().split()
print("Enter 3 index labels: ")
indices = input().strip().split()
try:
    if len(names) !=3 or len(indices)!=3:
        raise ValueError('please provide exact names with indices')
    series = pd.Series(data=names,index=indices)
    print("Created a new serice")
    print(series)
except ValueError as e:
    print(e)