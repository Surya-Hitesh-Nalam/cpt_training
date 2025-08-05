'''import pandas as pd
names = pd.Series(['apples','oranges','kiwi'])
df=names.to_frame(name="Name")
df['Price']=[50,30,80]
print(df)'''

import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    print(df)

    grouped = df.groupby('Department')['Bill'].mean()
    print(grouped)

except FileNotFoundError:
    print("Data not found")