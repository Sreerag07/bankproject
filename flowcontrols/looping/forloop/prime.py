num=int(input("Enter a number"))
res=0
for i in range(2,num):
    if(num%i==0):
        res+=1
if(res>0):
    print("not prime")
else:
    print("Is prime")