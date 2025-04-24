# # If we want to iterate index aswell as the elements in the list.

# li = [10,20,30,40,50]

# # If we want to work with both index and the elements in it we use Enumerate.
# for idx,ele in enumerate(li):
#     print(idx,ele)


# Write a python program to print all even index elements.

li = [10,20,40,60,70,33,54,6,89,0,34,51,27,83]

for i,j in enumerate(li,start=1): # In i the indexes are stored and in j the elements are stored. Here we used start = 1 so the list indexes are started with 0.
    if i%2 == 0:
        print(j,end= " ")

        