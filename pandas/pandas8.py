import pandas as pd
data={'name':["jeeva","kalai","yoge","vasim"],'age':[21,22,21,21],'location':['salem','chennai','salem','kovai']}
df=pd.DataFrame(data,index=[1,2,3,4])
#print(df)
percentage=[89,98,89,87]
df['Percentage']=percentage
#print(df)
print(df.loc[3])