# list=[1,2,3,5,55,44,22,66,88]
# def linear(x):
#     if x in list:
#         print("Number found")
#     else:
#         print("Not found")
# num=int(input("Enter number"))
# linear(num)
list=[1,2,3,5,55,44,22,66,88]
def linear(x):
    flag=0
    for i in list:
        if i==x:
            flag=1
            break
    if flag==1:
        print("Found")
    else:
        print("Not found")
num=int(input("Enter number"))
linear(num)