# Count Even and Odd Elements In the Tuple:
num_list = tuple(map(int, input().split()))
even = 0
odd = 0
for i in num_list:
    if i%2 == 0:
        even = even+1
    else:
        odd = odd+1
print(f"Number of even elements: {even}")
print (f"Number of odd elements: {odd}")