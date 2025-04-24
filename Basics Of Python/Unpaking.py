# Unpacking in Python refers to the process of assigning values from a collection (like a list, tuple, or dictionary)
# to multiple variables in a single statement. 

# One way is:
list_1 = ['charan',23,5.7]
name,age,height = list_1
print(name)
print(age)
print(height)

# Second Way of Unpacking:

li = ['charan',20,30,40,50]
name,*marks = li # * this symbole mean pack.
print(name)
print(marks)

# Third Way of Unpacking:

li = ['Charan',100,75,45,34,23]
name,*marks,age = li
print(name)
print(marks)
print(age)
