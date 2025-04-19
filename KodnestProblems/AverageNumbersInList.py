# Average numbers in a list:
number_list = list(map(int, input() .split))
sum_list = 0

for i in number_list:
    num = i
    sum_list = i +sum_list
average_list = sum_list / len(number_list)
print(f"The average of the list is: {average_list}")