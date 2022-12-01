import pandas as pd
df=pd.read_json('sample.json')
print(df.to_string())