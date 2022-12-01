import pandas as pd
mymarks={

     'jeeva':[98,78,90],
     'kalai':[78,67,90],
     'vasim':[89,90,98],
      'kavi':[89,76,78]
      }
marks=pd.Series(mymarks)
#print(marks)
print(marks['kavi'])