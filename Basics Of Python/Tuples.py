
'''
In tuple we can store Homogeneous as well as heterogeneous Data.
In tuples we can store duplicates.
Tuples are Ordered collection of Data
Tuples are immutable :  Once we declare we cannot modify it.
'''
tup1 = (10,22.2,'Saicharan',True,10)
print(tup1) # Output: (10, 22.2, 'Saicharan', True, 10)

# tup1.append(400) # Output : 'tuple' object has no attribute 'append'
# tup1.remove(10) # Output : 'tuple' object has no attribute 'remove'  
'''
In tuples we cannot add or remove the data because it is immutable.
But we can access the data 
'''
print(tup1[0]) #Output : 10
print(tup1[3]) #Output : True

del tup1 # Deletes the entire element
#print(tup1) 

#Manipulation in Tuples are not allowed.

# Concatinaion of the tuple:
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

# Interview Question:
# Create singleton tuple
tup = ('SaiCharan',)
print(tup,type(tup))
'''
While declaring the singleton tuple it is mandatory to use ',' otherwist 
it will be treated as as string, or integer what the data we are given.

'''
# Unpacking of Tuple.
new_tuple = (10,20,30,40)
# ele1 = new_tuple[0]
# ele2 = new_tuple[1]
el1,el2,el3,el4 = new_tuple
print('Value od el1 is:',el1)


