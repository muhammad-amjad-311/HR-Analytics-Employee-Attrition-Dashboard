import pandas as pd
df=pd.read_csv("HR_Analytics.csv")
print(df.info())
print(df.describe())
df1=df.duplicated().sum()
print(df1)
