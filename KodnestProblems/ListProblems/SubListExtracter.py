# Extract Sublit using string slicing:
number_list = list(map(int, input() .split()))
sub_list = []
start_index = int(input())
end_index = int(input())

sub_list = number_list[start_index : end_index]

print(f"Extracted sublist: {sub_list}")