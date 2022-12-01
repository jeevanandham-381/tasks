import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(70)
print(stack.get())
print(stack.get())
print(stack.get(timeout=1))
