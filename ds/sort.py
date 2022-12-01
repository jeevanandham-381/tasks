#input=[1,2,3,4,5,6],[4,5,6,7,8] output=[1,2,3,4,5,6,7,8]



import numpy as np

list1=[1,2,3,4,5,6,7]
list2=[4,5,6,7,8,9]
list3=np.concatenate((list1,list2))
#print(set(list3))
print(list(set(list3)))
