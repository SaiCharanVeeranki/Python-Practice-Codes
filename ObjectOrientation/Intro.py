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
# __init__
# __add__
# __str__

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name,"is Working")
e1 = Employee('Pooja',24)
