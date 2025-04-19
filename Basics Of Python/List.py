
'''
In list we can store homogeneous as well as Heterogeneous Data.
In list we can store Duplicate Values.
List is an 'ordered collection' of Data.(Order of insertion will remain
 as it is in the Output)
Lists are mutable :  One we create we can modify it.

'''
l1 = [10,20,30,True,'Kodnest']
print(l1,type(l1))
print(id(l1))
# Append
l1.append(300) # It will add element at the end of the list.(only accept one parameter at a time)
print(l1)
print(id(l1)) 
# Insert
l1.insert(1,15) # Add the element where ever we want ex: 'insert(index,value)'
print(l1)
# Remove
'''
By Default without parameters it wont remove any values 
if we dont give any parameter it wiil throw an error.
Atleast we should give one parameter.
'''
l1.remove(20) #ex: .remove(arg)
print(l1)
"""
It removes the first occerance of the specified element.
If we remove the element that is not present in th list it will through an error.
"""
# IN and Not IN Operators: (Membership Operators)
print(2000 in l1) #False
print('Kodnest' in l1) #True

# Pop() with out argument
removed_element = l1.pop() 
print(removed_element)
print(l1)

'''
With out Parameters It will delete and return the last element from the list.
'''
# Pop() With argument
'''
With argument it will Delete and return the specified index value.
'''
removed_element2 = l1.pop(4)
print(removed_element2)
print(l1)

# Difference b/w Remove and POP:
'''
Remove method dont return any values
but pop returns values

Remove accepts element as an argument
but pop accepts index values as an argument

remove wont work with out argument
but if we dont give any argument then pop will remove the last element.

'''

# del keyword:
del l1[1]
print(l1)
'''
Del keyword wont return any values 
but pop will return value

in real world if we want to work with deleted elements also 
in sudh sittuations we use pop else we use del.
'''

'''
del l1
print(l1) # In this case it will give you an error.

'''
