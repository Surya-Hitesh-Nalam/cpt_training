import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    series = df['Bill']
    print("\n Original Hospital Dataframe")
    print(series)

    print("\n Enter patient_ID to update")
    patient_id = input().strip()
    print("Enter new bill for {patient_id}:")
    new_cost = float(input())

    if patient_id in df['Patient_ID'].values:
        index = df[df['Patient_ID'] == patient_id].index[0]
        series[index]=new_cost
        print("\n Updated Medical Bill Series")
        print(series)
        df['Bill']=series
        df.to_csv('Hospital_data_updated.csv', index=False)
        print("\n Updated DataFrame saved to 'Hospital_data_updated.csv'")
    else:
        print(f"Error: patient_ID {patient_id} not found")
except FileNotFoundError:
    print("Data not found")