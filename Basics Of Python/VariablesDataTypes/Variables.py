'''
Variable Assigning:
<variable name> = <value>
Python uses = to assign values to variables.
There's no need to declare a variable in advance (or to assign a datatype to it), assigning a value to a variable itself declares and initializes the variable with that value.
There's no way to declare a variable without assigning it an initial value
'''
# Integer
a = 2
print(a)
Output: 2
# Integer    
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String    
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean    
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)
# Output: None

'''
Rules for variable naming:
1.Variables names must start with a letter or an underscore.
x  = True   # valid
_y = True   # valid

The reminder of your variable name may consist of letters, numbers and underscores. 
has_0_in_it = "Still Valid"

3. Names are case sensitive.
x = 9  
y = X*5  
=>NameError: name 'X' is not defined

Even though there's no need to specify a data type when declaring a variable in Python, while allocating the
necessary area in memory for the variable, the Python interpreter automatically picks the most suitable built-in
type for it:

a = 2
print(type(a))
# Output: <type 'int'>
b = 9223372036854775807
print(type(b))
# Output: <type 'int'>
pi = 3.14
print(type(pi))
# Output: <type 'float'>
c = 'A'
print(type(c))
# Output: <type 'str'>
name = 'John Doe'
print(type(name))
# Output: <type 'str'>
q = True
print(type(q))
# Output: <type 'bool'>
x = None
print(type(x))
# Output: <type 'NoneType'>

When you use = to do an assignment operation, what's on the left of = is a name for the object on the right.
Finally,what = does is assign the reference of the object on the right to the name on the left.
That is:
a_name = an_object  # "a_name" is now a name for the reference to the object "an_object
'''
#  We can assign multiple values to multiple variables in one line
a, b, c = 1, 2, 3
print(a, b, c) # Output: 1 2 3

a, b, c = 1, 2
# Traceback (most recent call last):
# File "name.py", line N, in <module>
# a, b, c = 1, 2
# ValueError: need more than 2 values to unpack
a, b = 1, 2, 3
# Traceback (most recent call last):
# File "name.py", line N, in <module>
# a, b = 1, 2, 3
#  ValueError: too many values to unpack



# a = 10
# b = 20

# print("Addition of a and b :",a+b)


# message = "Veeranki sai charan"
# print(len(message))

# message = "Veeranki Sai Charan"
# capital_text = message.upper()
# print(capital_text)

# message = "VEERANKI SAI CHARAN"
# lower_string = message.lower()
# print(lower_string)

# text  = "My name is sai charan and i am from vijayawada"
# print(text.find("VIJAYAWADA"))
# print("VIJAYAWADA" in text)


sentence = "I love java and i have a good knowledge in java"
modified_sentence = sentence.replace("java","python")
print(modified_sentence)