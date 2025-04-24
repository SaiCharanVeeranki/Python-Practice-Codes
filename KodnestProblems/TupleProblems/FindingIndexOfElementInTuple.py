# Find the index of an Element in a Tuple:
Num_tuple = tuple(map(int, input().split()))
Enter_num = int(input())

if Enter_num in Num_tuple:
    print(f"The index of {Enter_num} in the tuple is: {Num_tuple. index(Enter_num) }")
else:
    print(f"{Enter_num} is not in the tuple.")

