# Find Symmetric Difference Between two sets
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
sys = set(list_1).symmetric_difference(set(list_2))
sys = sorted(sys)

print(f"Symmetric difference of elements: {sys,type(sys)}")