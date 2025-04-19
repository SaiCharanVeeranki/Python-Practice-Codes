# List of squres using list conprinsion:
number_list = list(map(int, input() .split()))

squre_list = [i ** 2 for i in number_list]

print(f'List of squares: {squre_list}')