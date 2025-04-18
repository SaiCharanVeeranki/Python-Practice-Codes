'''
In Set We can Store Homogeneous and hetrogeneous type od Data.
In Set We cannot store Duplicate values.
Set is an unordered collection of data.
Set does not support indexing of data.
Sets are mutable.
'''
s1 = {10,True,10,'Charan',44.10}
print(s1,type(s1)) #Output: {'Charan', True, 10, 44.1} <class 'set'>
 
# add(): Used to add an element in the set.
s1.add(500)
print(s1)

s1.remove(500)
print(s1)

removed = s1.pop() # He if we use pop with index value it wont work.
print(removed)
print(s1)
# Pop without index it will delete and return one element

del s1