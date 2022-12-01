import json
stu_data='''
{
    "details" : [
    {
    'name':'jeeva'
    'age'=21
    'location':"salem"
    },
    {
    'name':'kalai'
    'age'=21
    'location':"salem"
    }
    ]
}
'''
print(type(stu_data))
data = json.loads(stu_data)

print(type(data))