# val1 = "veeranki"
# print(val1,id(val1))
# val1 = val1.upper()
# print(val1,id(val1))

'''
Strings are Immutable:
Python strings are immutable, meaning once a string is created, it cannot be changed.
If you try to modify a string, Python creates a new string instead of modifying the original.

If new String doesnot have any referance variables then it will be removed by Garbage Collector.

String Interning is a process of checking string intern pool before creating the new object.

Whenever we want to creat a new object, Python first will check String intern pool, weather that object is alredy exist or not.

when object already exist in the string intern record the the adress of existing object will be reused.

'''



# s1 = 'Hello'
# s2 = 'World'

# print(s1,id(s1))
# print(s2,id(s2))

# print(f"The address of H in s1 is: {id(s1[0])}")


# print(f"The address of o in s1 is: {id(s1[-1])}")
# print(f"The address of o in s2 is: {id(s2[1])}")


# print(f"The address of l in s1 is: {id(s1[2])}")
# print(f"The address of l in s1 is: {id(s1[3])}")
# print(f"The address of l in s2 is: {id(s2[3])}")

long_str1 = "this_is_a_very_long_string_that_Python_may_not_intern"
long_str2 = "this_is_a_very_long_string_that_Python_may_not_intern"
print(id(long_str1),id(long_str2))  # False (Python avoids interning long strings)

'''

'''

