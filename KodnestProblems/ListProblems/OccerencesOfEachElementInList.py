# Occurences of each number in the list:
num_list = list(map(int, input().split()))

dict_1 = {}
for i in num_list:
    if i in dict_1:
        dict_1[i] = dict_1[i] + 1
    else:
        dict_1[i] = 1

for num, count in dict_1.items ():
    print(f"{num} occurs {count} time(s)")