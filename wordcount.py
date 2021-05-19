a={}
f=open("text1","r")
b=""
count=0
for i in f:
    wr= i.split()
for word in wr:
    if word not in a:
        a.update({word:1})
    else:
        val=int(a[word])
        val+=1
        a.update({word:val})
print(a)