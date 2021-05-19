class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print("age",self.age)
    def __str__(self):
        return self.name
f=open("student.txt","r")
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    st=Student(name,age)
    print(st)
    st.printvalue()

