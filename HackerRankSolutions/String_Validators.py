# print('Kodnest1234*'.isalnum()) #Flase
# print('Kodnest1234'.isalnum()) #True

# print('Charan'.isalpha()) #True
# print('Charan12'.isalpha()) #Flase

# print('12'.isdigit()) #True

# print('Charan12'.isupper()) #False
# print('CHARAN12'.isupper()) #True

# print('charan12'.islower()) #True


# print(any([10,20]))
# print(any([True,False,False,False])) #True
# print(any((False,False,False,False))) #Flase

# ------------------LOGIC-------------------------------------------------------------

s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s])) 
print(any([i.isupper() for i in s])) 
print(any([i.islower() for i in s])) 