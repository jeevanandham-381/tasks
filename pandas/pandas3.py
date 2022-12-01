import pandas as pd
climate={
    'weather':[34,45,43],
    'place':['salem','kovai','vellore']
    }
wt=pd.DataFrame(climate,index=[1,2,3])
print(wt.loc[[1]])
