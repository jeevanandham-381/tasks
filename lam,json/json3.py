#deserilaization
import json
with open('emp.json','r') as j:
    new1=json.load(j)

#new1=json.loads(employee_str)
print(type(new1))
#print("name:",new1['name'])
#print("place:",new1['place'])
#print("is married:",new1['ismarried'])
for k,v in new1.items():
    print('{}:{}'.format(k,v))
