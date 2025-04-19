# a = input("Enter a Number: ")
# print(f"The number is: {a},The data Type of {a} is: {type(a)}")

# '''
# In Python, the input() function by default stores the user input as a string (str).
# No matter what the user enters, it is always treated as a string unless explicitly converted to another data type.

# '''
# #Type Casting:

# number = int(input("Enter a number: "))
# print(f"The Value is:  {number} and Data Type is: {type(number)}")


# Addition of two numbers using input function

Number1 = int(input("Enter your First Number: "))
Number2 = int(input("Enter your Second Number: "))

Sum = Number1 + Number2
sub = Number1 - Number2
mult = Number1 * Number2
div = Number1 / Number2
print(f"Sum of two numbers {Number1} + {Number2} is : {Sum}") # 30
print(f"Substration of two numbers {Number1} + {Number2} is : {sub}") #10
print(f"Multlipication of two numbers {Number1} + {Number2} is : {mult}") #200
print(f"Division of two numbers {Number1} + {Number2} is : {div}") #2.0

#In python the result of Division will always be of type float
