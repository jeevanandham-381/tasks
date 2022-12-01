import ds6 as j
#print("enter ypur option: ")
while True:
    option=input("enter ypur option:")
    if option=="add":
        j.enqueue()
    elif option=="delete":
        j.dequeue()
    elif option=="show":
        j.display()


