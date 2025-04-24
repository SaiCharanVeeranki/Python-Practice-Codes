s1 = set(map(int,input() .split()))
s2 = set(map(int, input().split()))

if s1.isdisjoint(s2):
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")