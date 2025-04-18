'''
There are three types of Control Constructs
1.Conditional Control Constructs - if-else, if-elif
2.Looping Control Constructs - for,while
3.Jumping Control Constructs - Break,Continue,pass
'''
# def check_age(age):
#     if age > 18:
#         print("Age is greater than 18")
#     else:
#         print("Age is not greater than 18")
# check_age(18)

def displayAgeCatagory(age):
    if age < 18:
        print("Child")
    elif age > 18 and age < 65:
        print("Adult")
    elif age > 18:
        print("Senior Citizen")
        
displayAgeCatagory(int(input("Enter age: ")))
