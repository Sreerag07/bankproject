#add two  numbers
# def add(num1,num2):#these are parameters
#     return num1+num2
# res=add(10,20)#10 and 20 are arguments
# print(res)

#add three numbers
# def add_three(num1,num2,num3):
# #addThree()-camalin notation
# #add_three()-snake notation
#     return num1+num2+num3
# result=add_three(2,3,4)
# print(result)
#variable length argumeents are used to create one functions that add any number of arguments
def add(*args):
    res=0
    for num in args:
        res+=num
    print(res)
add(1,2,3)
add(1,2)
add(1)