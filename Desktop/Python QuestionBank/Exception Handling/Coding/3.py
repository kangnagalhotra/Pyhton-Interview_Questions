# Create a custom exception NegativeNumberError and use it.

class NegativeNumberError(Exception):
    pass
def square_num(n):
    if n<0:
        raise NegativeNumberError("Negative numbers not allowed")
    else:
        return n*n
    
try:
    num=  int(input("Enter number"))
    result = square_num(num)
except NegativeNumberError:
    print("Negative number ")
else:
    print("Square of number: ", result)