def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select the operator(+,-,*,/)")
print("1.add,2.sub,3.mul,4.div")
while True:
    choice=input("Enter choice")
    if choice in("1","2","3","4"):
        num1=float(input("Enter 1st"))
        num2=float(input("Enter 2nd"))
        if(choice=="1"):
            print(add(num1,num2))
        elif(choice=="2"):
            print(sub(num1,num2))
        elif(choice=="3"):
            print(mul(num1,num2))
        elif(choice=="4"):
            print(div(num1,num2))
        else:
            print("Invalid operator")