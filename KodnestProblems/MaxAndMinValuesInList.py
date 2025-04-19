# Maximum and Mininum Values in  the list:
num_list = list(map(int, input().split()))

num_list.sort(reverse = True)
max = num_list[0]
print(f"The maximum value is: {max}")
num_list.sort()
min = num_list[0]
print(f"The minimum value is: {min}")