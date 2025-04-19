# Dict is mutable
d1 = {'name':'priya','name':'priya','age':22, 'phoneno':9.587}
print(d1) #{'name': 'priya', 'age': 22, 'phoneno': 9.587}

d1['name'] = 'pooja'
print(d1) #{'name': 'pooja', 'age': 22, 'phoneno': 9.587}

d2 = {'name': 'Charan', 'age': 21, 'phn' : 12234, 'age': 23}
print(d2) #{'name': 'Charan', 'age': 23, 'phn': 12234}

'''
In dict we cannot store duplicate keys.
'''
# In dict we can store dupicate values.
marks = {'sci':85,'mat':85} #Allowed

d1['phoneno'] = 9589776669
print(d1)

for i in d1.keys(): # This will retrive the keys
    print(i,type(i))

for i in d1.values(): # this will retrive the values
    print(i, type(i))

for i in d1.items(): # this will retrive both.
    print(i,type(i))
# The output of the above will be presented in tuples. 


list(),tuple(),set(),dict()

int(),float(),str(),bool(),complex()