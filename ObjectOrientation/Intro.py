class Student:
    def learn(self):
        print(self.name,"is learn")
    def play():
        print("Inside Play Method")
s1 = Student()
s1.name = 'Pooja'
print("Name is",s1.name)
s1.learn()
# s1.play() # takes 0 positional arguments but 1 was given

# Dunder Methods or Magic Methods:
# __init__ it is the Construncter in python
# __add__
# __str__

class Employee:
    def __init__(self,name,age): #Has part
        self.name = name
        self.age = age
    def work(self): #Does part
        print(self.name,"is Working")
e1 = Employee('Pooja',24)

# Can we write object name in the place of Self.name as e1.name?
'''
No, We can write
But it is not the effective way of writing 
because for every object the e1 details got printed
if you dont want that then we should use self only.
'''