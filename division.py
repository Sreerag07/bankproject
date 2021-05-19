num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
    print(num1/num2)
except:
    print("Exception occured")
#unexpected errorss are handled by exception handling
#these are done by try and catch
#only one block will work at a time