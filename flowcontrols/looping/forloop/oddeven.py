num1=int(input("Enter lower"))
num2=int(input("Enter upper"))
odd=0
even=0
for i in range(num1,num2+1):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
print("Even sum:",even)
print("Odd sum:",odd)