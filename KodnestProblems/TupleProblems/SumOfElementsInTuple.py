# Sum of all elements in the Tuple:
num_tuple = tuple(map(int, input() .split()))
sum_ele = 0
for i in num_tuple:
    sum_ele += i
print(f"The sum of the elements in the tuple is: {sum_ele}")