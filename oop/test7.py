f=open("phn.txt","r")
lst=[]
for i in f:
    lst.append(i.rstrip("\n"))
import re
x='(\+91)\d{10}$'
for j in lst:
    match=re.fullmatch(x,j)
    if match is not None:
        d=open("phnvalid.txt","a")
        d.write(j)
        d.write("\n")
        d.close()