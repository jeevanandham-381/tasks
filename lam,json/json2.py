#serialization
#pythn dict to json
import json
employee={'name':'jeeva',
          'age':21,
          'place':'salem',
          'ispurshing':False,
          'ismarried':None
          }
new=json.dumps(employee,indent=4)
print(new)

with open('emp.json','w') as j:
    json.dump(employee,j,indent=4)


