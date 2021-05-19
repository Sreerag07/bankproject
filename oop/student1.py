class Student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("Department:", self.dep)
        print("mark:", self.mark)
    def __str__(self):
        return self.name
f=open("dep.txt","r")
for line in f:
    data=line.rstrip("\n").split(",")
    if(int(data[3])>190):
        name=data[0]
        rollno=data[1]
        dep=data[2]
        mark=data[3]
        st=Student(name,rollno,dep,mark)
        print(st)
        st.printvalue()

