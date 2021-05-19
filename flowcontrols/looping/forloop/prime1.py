
min=int(input("Enter min"))
max=int(input("Enter max"))
sum=0
for a in range(min,max):
    if(a>1):
        for i in range(2,a):
            if(a%i==0):
                break
        else:
            print(a)
            sum+=a
print("sum of  numbers",min,"to",max,"is",sum)