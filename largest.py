a=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
a.sort()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
c=len(b)
max=b[c-2]
print(max)

