#Iterable Objects:
# list
# string 
# tuple
# set
# range()

# List Method:
# list(iterable_objects)
'''
In list method will only allowed to pass iterable objects only.
'''
# l1 = list(5) #error : 'int' object is not iterable

l2 = list('charan')
print(l2) # ['c', 'h', 'a', 'r', 'a', 'n']

l3 = list((10,3.24,'charan'))
print(l3) # [10, 3.24, 'charan']

l4 = list({12,'kund',33.5})
print(l4) # [33.5, 12, 'kund']

l5 = list({'name': 'priya','age' : 23})
print(l5) # ['name', 'age']
# When we are converting dict into list it will show the keys only.

l6 = list(range(1,11))
print(l6)

# Tuple method:
# tuple(iterable_objects)

tup1 = tuple([10,2.2,'charan'])
tup2 = tuple({100,200})
tup3 = tuple({'name': 'Charan','age' : 22}) 
tup4 = tuple('Charan')
tup5 = tuple(range(1,11))

print(tup1)  #(10, 2.2, 'charan')
print(tup2)  # (200, 100)
print(tup3) #('name', 'age')
print(tup4) #('C', 'h', 'a', 'r', 'a', 'n')
print(tup5) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Set Method
# set (iterable_object)

s1 = set('Charan')
print(s1) #{'a', 'r', 'C', 'n', 'h'} removes duplicates and return unordered set.

# Dist Method:
# dict(iterable_objects: key:value)

d1 = dict([['name','priya'],['age',22],])
print(d1)

