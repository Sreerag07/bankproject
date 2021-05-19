#swapping
#(no1,no2)=(no2,no1)
#factorial
fact=1
num=int(input("Enter a number"))
if num<0:
    print("Factorial does not exist")
elif num==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)