import pandas as pd
data={
    "tamil":{
        "jeeva":90,
        "kalai":87,
        "vasim":78,
    },
    "english":{
        "jeeva":89,
        "kalai":87,
        "vasim":78,
    },
    "maths":{
        "jeeva":89,
        "kalai":87,
        "vasim": '',
    },

}
data1 = {
    k: None if not v else v for k, v in data.items()
}
df=pd.DataFrame(data1)
#print(df)
df.fillna(89,inplace=True)
print(df)
#print(df.loc['jeeva'])
#print(df.info())