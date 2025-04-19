# #With out inout and with out return statment
# def add():
#     a = 10
#     b = 20
#     print(a+b)
# add()

# #With input and without return statment
# def sub(a,b):
#     print('Substraction is:',a-b)

# #without input and with return statment
# def mul():
#     return 10*20

# #With input and with return statment
# def div(a,b):
#     return a/b
# add()
# sub(20,10)
# mul()
# div(200,10)

# rows  = int(input())
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i == 1 or i == 4 or j == 1 or j ==4:
#             print("*", end="")
#         else:
#             print(" ",end = "")
#     print()


# Dimand
# rows = int(input())
# for i in range(1,rows+1):
#     for space in range(1,rows-i+1):
#         print(" ", end = "")
#     for star in range(1,i+1):
#         print("*",end = " ")
#     print()
# for i in range(1,rows+1):
#     for space in range(1,i+1):
#         print(" ", end = "")
#     for star in range(1,rows-i+1):
#         print("*",end = " ")
#     print()

# rows = int(input())

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
# for i in range(1,rows+1):
#     for j in range(i,rows+1-1):
#         print("*",end = " ")
#     print()

# rows = int(input())
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end = " ")
#     for space in range(i,rows-1):
#         print(" ", end = " ")
#     for space in range(i,rows-1):
#         print(" ", end = " ")
#     for j in range(i+1):
#         print("*",end = " ")
#     print()
# for i in range(rows-1):
#     for j in range(i,rows-1):
#         print("*",end = " ")
#     for space in range(i+1):
#         print(" ", end = " ")
#     for space in range(i+1):
#         print(" ", end = " ")
#     for j in range(i, rows-1):
#         print("*",end = " ")
#     print()

rows = int(input())
for i in range(rows):
    for space in range(i,rows-1):
        print(" ",end = " ")
    for star in range(i+1):
        print("*",end = " ")
    for star in range(i):
        print("*", end = " ")
    for space in range(i,rows-1):
        print(" ",end = " ")
    print()
for i in range(rows):
    for space in range(i+1):
        print(" ",end = " ")
    for star in range(i,rows-1):
        print("*",end= " ")
    for star in range(i,rows-2):
        print("*",end = " ")
    for space in range(i+1):
        print(" ",end= " ")
    print()
    