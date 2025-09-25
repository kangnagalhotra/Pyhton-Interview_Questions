# Use filter to extract only even numbers from a list.

num=[2,3,4,8,6,10,9]
evens = list(filter(lambda x:x%2==0 ,num ))
print(evens)