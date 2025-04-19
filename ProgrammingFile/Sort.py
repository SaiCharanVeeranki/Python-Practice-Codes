# Sort Method :
# object.Sort()
# Sort will modify the original message.
li1 = [10,5,3,20]
li1.sort()
print(li1) #[3, 5, 10, 20]

li1.sort(reverse = True)
print(li1) #[20, 10, 5, 3]

# Sorted Method

li2 = [100,30,500,10]
sorted_li2 = list(sorted(li2))
print(sorted_li2) #[10, 30, 100, 500]
# Sorted will create a new copy of the list.