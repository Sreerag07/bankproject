num1=int(input("Enter initial range"))
num2=int(input("Enter final range"))
for i in range(num1, num2):
    if(i%2!=0):
        for j in range(num1,num2):
            print()
            for k in range(0,j):
                print(i, end=" ")
    else:
        for j in range(num1,num2):
            print()
            for k in range(num2,j,-1):
                print(i,end=" ")
