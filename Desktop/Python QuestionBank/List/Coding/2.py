#Remove duplicates from a list (without set).

list = [1,2,2,2,3,3,4,5,6,6,7,7,7,8,8,9]
new_list=[]

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
