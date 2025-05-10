class Employee:
    company_name = "Code" #Class Based Variables.
    def __init__(self,name,age,desig):
        self.name = name #Instance based variables
        self.age = age
        self.desig = desig
    def login(self,time):
        print(f"{self.name} logged in at {time}")
    
    def work(self,hours):
        print(f"{self.name} is worked for {hours} Hours.")
    
    def logout(self,time):
        print(f"{self.name} logged out at {time}")
    
    def get_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee Designation: {self.desig}")

e1 = Employee("charan",22,"Sofwate Developer")
e2 = Employee("Deepu",25,"Manager")
e3 = Employee("Tharun",28,"Tester")

e1.get_details()
e2.get_details()
e3.get_details()
e1.login('10:15')