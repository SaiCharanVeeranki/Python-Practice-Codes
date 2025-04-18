# LIST SLICING: 
# list_name[start : end - 1 : steps]
l1 = [10,20,30,40,50,60]
sublist = l1[0:4:1]
print(sublist) #[10, 20, 30, 40]  
sublist1 = l1[::]
print(sublist1) #[10, 20, 30, 40, 50, 60]
sublist2 = l1[1::]
print(sublist2) #[20, 30, 40, 50, 60]
sublist3 = l1[::2]
print(sublist3) #[10, 30, 50]

# Reverse list 

reverse_list = l1[::-1]
print(reverse_list) #[60, 50, 40, 30, 20, 10]

print(l1[-1::]) #[60] #Corner case

'''
What is list slicing?
It is used to creat sublist from the main list.

list_name[start : end - 1 : step]
last element : [-1::]
'''
