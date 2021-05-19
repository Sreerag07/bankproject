class Student:
    def __init__(self,name,no,dep,mark):
        self.name=name
        self.no=no
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print("name",self.name)
        print("no",self.no)
        print("department",self.dep)
        print("mark",self.mark)
lst = []
f=open("std.txt","r")
for line in f:
    d=line.rstrip("\n").split(",")
    name=d[0]
    no=d[1]
    dep=d[2]
    mark=d[3]
    s=Student(name,no,dep,mark)
    lst.append(s)
print(lst)
mark1=[]
for st in lst:
    mark1.append(st.mark)
for st in lst:
    if(st.mark==max(mark1)):
        print(st.no,st.name,st.dep,st.mark)
#
#     lst.append(data)
# print(lst)
# for i in range(0, len(lst)):
#     for j in range(0, len(lst) - i - 1):
#         if lst[j][-1] > lst[j + 1][-1]:
#             temp = lst[j]
#             lst[j] = lst[j + 1]
#             lst[j + 1] = temp
# print("the details of Student with highest mark is ", lst[-1])