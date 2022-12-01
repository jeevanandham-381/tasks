queue=[]
def enqueue():
    element=input("enter the num to enqueue:")
    queue.append(element)
    print(element,"to a added queue")
def dequeue():
    if len(queue)==0:
        print("the queue is empty")
    else:
        d=queue.pop()
        print("the removed element",d)
def display():
    print("the queue is",queue)


