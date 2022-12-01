def Split(num):
    even_li = []
    odd_li = []
    for i in num:
        if i % 2 == 0:
            even_li.append(i)
        else:
            odd_li.append(i)
    print("Even lists:", even_li)
    #print("Odd lists:", odd_li)
    print("odd list:",list(set(odd_li)))
num = [1,1,2,3,4,5,6,7]
Split(num)