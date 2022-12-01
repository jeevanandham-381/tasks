value1 = ["1", "2", "3","4" ,"9"]
value2 = ["4", "6", "7", "8",""]

new_list = []
for i in range(0, len(value1)):
    new_list.append(value1[i] + value2[i])
   
#print ("the new list is : " + (str(new_list))) 
list= [round(float(i)) for i in new_list]
print(list)