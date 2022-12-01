list_of_list = [[1,2,3],[4,5,6]]
output_list = []

for newlist in list_of_list:
    output_list.append(list(map (lambda x: x**2,newlist)))

print(output_list)