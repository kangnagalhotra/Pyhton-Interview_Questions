# Write a recursive function to calculate Fibonacci numbers

def fibonaci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
num=int(input("enter number: "))
print(fibonaci(num))
        
    
    
    