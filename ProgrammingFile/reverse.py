# The reverse() it will reverse the original object.
# Syntax: object.reverse()
li = [10,5,20,7,40]
print(li)
li.reverse()
print('After reverse:,',li)

# Reversed:
# syntax: reversed(object) --->
li2 = [11,2,6,8,22]
reverse_li2 = list(reversed(li2))
print(li2) #[11, 2, 6, 8, 22]
# it returning iterator object
print(reverse_li2) #<list_reverseiterator object at 0x000001221284ADD0>
'''
The reversed method creates the new list.
The reversed method will return the iterator object.
if we want the reverse list we can use like:
reversed_list = list(reversed(li2)) This is how we specify.
'''

li3 = [1,5,2,9]
new_copy = list(reversed(li3))
print(new_copy) # Creating new list with out modifing the original list.
li3.reverse()
print(li3)# Reversing the original object or llist.
