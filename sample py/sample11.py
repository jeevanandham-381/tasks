#json to python
import imp


import json

#x = '{ "name":"Jeeva", "age":22, "city":"salem"}'

#y = json.loads(x)
#print(y["name"])

#python to json

p={"a":90,"s":1000,"d":30}

q=json.dumps(p,indent=2,separators=(".","="),sort_keys=True)
print(q)