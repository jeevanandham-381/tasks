import demo2 as x
import ds6 as j
print("queue application")
opt=int(input("enter 1.queue operation study 2.queue operation practice:"))
if opt==1:
    print("if you are enter yes,you will going to study page(geeksforgeeks) ")
    choice = input("enter yes or no:")
    if choice=='yes':
        x.page()
    else:
        print("you see in google")
        x.page2()
elif opt==2:
    while True:
        option = input("enter ypur option(add,delete,show):")
        if option == "add":
            j.enqueue()
        elif option == "delete":
            j.dequeue()
        elif option == "show":
            j.display()
        else:
            exit()