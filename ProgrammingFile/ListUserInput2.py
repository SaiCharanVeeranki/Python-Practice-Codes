l1 = input('Enter space seperated values: ')
# print(l1,type(l1)) #10 20 <class 'str'>
l1 = l1.split()
print(l1)
l1 = list(map(int,l1))
print(l1)

# Split() It convert string to list.

tup = tuple(map(int,input('Enter space seperated values: ').split()))
print(tup)


inp = list(map(int,input().split()))
print([i for i in inp if i%2 == 0])