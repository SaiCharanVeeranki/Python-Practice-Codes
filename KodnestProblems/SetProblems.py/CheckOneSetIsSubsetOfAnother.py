# Check if one set is sub set of another or not:
s1 = set(map(int, input() .split()))
s2 = set(map(int, input().split()))

if set(s1).issubset(s2):
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")


