


def factorial(x):
    if x==1:
        return 1
    elif x<0:
        return("not valid")
    else:
        return ( x * factorial(x-1))
x=int(input("enter the num:"))
result=factorial(x)
print (x,"factorial is" , result)


