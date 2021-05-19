num1=10
num2=20
#numbers before swapping
print("Numbers before swapping")
print("Number 1 is ",num1)
print("Number 2 is ",num2)
print("Numbers after swapping")
temp=num1
num1=num2
num2=temp
print("Number 1 is ",num1)
print("Number 2 is",num2)
num1,num2=num2,num1
print("Number 1 is ",num1,"Number 2 is ",num2)
#using operators
num1=num1+num2#10+20=30
num2=num1-num2#30-20=10
num1=num1-num2#30-10=20