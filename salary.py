lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
d=[]
for i in lst:
    d.append(i[3])
print(d)
for i in lst:
    if(i[3]==max(d)):
        print(i)