# Reverse a List using list slicing.
number_list = list(map(int, input() .split()))
reversed_list = number_list[: : -1]
print(f"Reversed list: {reversed_list}")