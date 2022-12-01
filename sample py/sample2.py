num=int(input("enter the num:"))
flag=False
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            
if flag:
    print(num,"is a prime")
else:
 print(num,"is not a prime")