def left_join(l1, l2):
    f_len = len(l1)-(len(l2) - 1)
    for i in range(0, len(l2), 1):
        if f_len - i >= len(l1):
            break
        else:
            l1[i] = l1[i] + l2[i]
    return l1
list1=['1','2','3','4','5']
list2=['5','6','7','8']
list3=[]
list3.append(left_join(list1,list2))
print(list3)
