#Rotate a list by k positions.

list=[1,2,3,4,5]
k=int(input("enter value of k :"))
k=k%len(list)
rotated_list = list[-k:]+list[:+k]
print(rotated_list)