num=int(input('enter the num:'))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10

if num==sum:
        print(num,"armstorng num")
else:
        print(num,"not armstorng num")     