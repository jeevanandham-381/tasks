import pandas as pd

student_data = {
  'name': ["jeeva", "kalai", "vasim","karthik","kavi","mano"],
  'marks': [75, 79, 82,89,76,89],
  'attedence':[90,89,90,98,89,90],
}

myvar = pd.DataFrame(student_data)

print(myvar)
