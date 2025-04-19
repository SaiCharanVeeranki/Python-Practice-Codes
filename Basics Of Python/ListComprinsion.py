l1 = [1,2,3,4,5]
squre_list = [] 
for i in l1:
    squre_list.append(i**2)
print(squre_list)
'''
Here we have return 5 lines of code but if we use list comprinsion we can 
write the same code in 2 lines.
'''
# LIST COMPRINSION:
# Syntax:
# [Expression for i in iterable_object condition]

l1 = [1,2,3]

new_list1 = [i for i in l1]
print(new_list1)
squre_l = [i**2 for i in l1]
sum_2 = [i+2 for i in l1]

print(new_list1) #[1, 2, 3]
print(squre_l) #[1, 4, 9]
print(sum_2) #[3, 4, 5]

# Using Condition:
l1 = [1,2,3,4,5,6,7,8,9,10]
even_l = [i for i in l1 if i%2 ==0]
print(even_l) #[2, 4, 6, 8, 10]


l1 = [1,2,3,4,5]
squre_list = [] 
for i in l1:
    squre_list.append(i**2)
print(squre_list)
'''
Write the above code using list comprinsion?
'''
squre_l = [i**2 for i in l1]
print(squre_l)

'''
If we have if and else both in list comprinsion Then the sentax looks:
'''
# ['expression if True' condition 'Expresion if false' for i in iterable_object]
even_odd = ['even' if i %2 == 0 else 'odd' for i in l1]
print(even_odd)

# If we are having only one condition then code look like:
squre_l = [i**2 for i in l1]
# if 2 conditions

# Multiple for loops inside list Comprinsion:

li = [[10,20],[30,40],[50,60]]

new_li = [ele for i in li for ele in i]
print(new_li)

