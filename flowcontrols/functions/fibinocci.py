n=int(input("Enter range"))
a=0
b=1
count=0
for i in range(0,n+1):
    print(a)
    count=a+b
    a=b
    b=count
    count+=1



