#Flatten a nested list.

nested_list = ['34,45,"hello',[1,2,3,4],["python",5.6]]
flat_list=[]

for i in nested_list:
    if isinstance(i,list):
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)
print(flat_list)
            

#isinstance(i, list) → checks if i is a list.
    #If it is, we loop through its elements (j) and append each element individually to flat_list.