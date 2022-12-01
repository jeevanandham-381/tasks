def leap():
    year=int(input("enter the year:"))
    for year in range(year,year+3):
        if(year%400==0 and year%100==0):
            print(year,"is a leap year")
        elif(year%4==0 and year&100 != 0):
            print(year,"is a leap year") 
        else:
             print(year,"not a leap year")

                