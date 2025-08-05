import numpy as np
import pandas as pd
series = pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
print("Original Series:")
print(series)

# check missing values
print("Missing values")
print(series.isna())

#replace nan with 0
filled_series = series.fillna(0)
print("\n series after filling NaA with 0:")
print(filled_series)