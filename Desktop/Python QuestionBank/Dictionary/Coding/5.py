# Create a dictionary of squares from 1 to n.

n = int(input("Enter a number: "))
squares = {i: i**2 for i in range(1, n+1)}
print(squares)
