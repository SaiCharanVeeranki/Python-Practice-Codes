n = int(input())
l1 = []

for i in range(n):
    operation = input()
    opp = operation.split()
    if 'insert' in opp:
        l1.insert(int(opp[1]),int(opp[2]))
    elif 'print' in opp:
        print(l1)
    elif 'remove' in opp:
        l1.remove(int(opp(1)))
    elif 'append' in opp:
        l1.append(int(opp[1]))
    elif 'sort' in opp:
        l1.sort()
    elif 'pop' in opp:
        l1.pop()
    elif 'reverse' in opp:
        l1.reverse()

