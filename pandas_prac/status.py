import pandas as pd
try:
    df= pd.read_csv("hospital_data.csv")
    print("\n Original hospital DataFrame:")
    print(df)

    df['Status']=df['Age'].apply(lambda x: 'Senior' if x>=50 else 'Adult' if x>=18 else 'Minor')
    print("\n DataFrame with Status column")
    print(df)

    df.to_csv('Hospital_data_updated.csv',index=False)
    print("\n Updated DataFrame saved to 'Hospital_data_updated.csv'")
except FileNotFoundError:
    print("Data not found")