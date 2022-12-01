import pandas as pd

df = pd.read_csv('data,csv')
#print(df)
for x in df.index:
    if df.loc['Duration']<120:
        df.loc['Duration'] = 120

print(df.to_string())
#print(df.drop_duplicates())
