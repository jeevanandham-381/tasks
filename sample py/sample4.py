def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

def main():
    n_val =int (input("enter the n:"))
    if n_val <0:
     print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for n in range(n_val):
            print(fibo(n))