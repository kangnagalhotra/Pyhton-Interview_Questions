#Print Fibonacci sequence up to n.

n=int(input("Enter n: "))
a=0
b=1
while a<=n:
    print(a)
    a,b=b,a+b
