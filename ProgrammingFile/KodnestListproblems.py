li = list(map(str,input().split()))
dict1 = {}

for ele in li:
    if ele in dict1:
        dict1[ele] = dict1[ele]+1
    else:
        dict1[ele] = 1
for ele,count in dict1.items():
    print(f'{ele}: {count}')
