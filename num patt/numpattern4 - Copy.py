#input=12345,goods
num=input("enter input:")
length=len(num)
for i in range(length):
    for j in range(length):
        if (i==j or i+j==length-1):
            print(num[j],end=' ')
        else :
            print(' ',end=' ')
    print()
