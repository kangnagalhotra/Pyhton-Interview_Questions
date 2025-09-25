# Extract the nth element from each tuple in a list of tuples.

tup_list=[(1,2,3),(8,9,10),(7,0)]
n=1 
nth_element = [t[n] for t in tup_list]
print(nth_element)
