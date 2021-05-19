num1=int(input("Enter numbr 1"))
num2=int(input("Enter numbr 2"))
num3=int(input("Enter numbr 3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("Largest number is",num2)
    else:
        print("Largest is ",num3)
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print("Largest number is",num1)
    else:
        print(num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("Largest number is",num1)
    else:
        print(num2)