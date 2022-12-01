import pandas as pd
data1={'name':["jeeva","kalai","yoge","vasim"],'age':[21,22,21,24],'location':['salem','chennai','salem','kovai']}
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
        'Age':[17, 14, 12, 52],
        'location':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj']}
df1=pd.DataFrame(data1,index=[1,2,3,4])
df2=pd.DataFrame(data2,index=[5,6,7,8])
#print(df)
#print(df.loc[True])
#print(df['age']>21)
#new=df.index<=3
print(df1,"\n\n",df2)
#frames=([df1,df2])
res3 = pd.concat([df1,df2])

print(res3)
#df.groupby('name')
#print(df.groupby(['name']).sum())