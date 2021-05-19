# def star():
#     for i in range(1, 6):
#         for j in range(1, (i + 1)):
#             print("*", end=" ")
#         print()
# star()
# def pattern(n):
#     for i in range(0,n):
#         for j in range(0,(i+1)):
#             print("*",end=" ")
#         print()
# pattern(5)

def pattern():
    for i in range(1,6):# 1 2 3
        print()
        for j in range(6,i,-1):#5 4 3 2 1
            print("*",end=" ")

pattern()
