# Find repeated elements in a tuple.

tup = (1, 2, 3, 3, 3, 2, 4)
seen = []      
repeats = []   

for i in tup:
    if i in seen and i not in repeats:
        repeats.append(i)
    else:
        seen.append(i)
new_tup = tuple(repeats)
print("Repeated elements:", new_tup)


