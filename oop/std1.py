class Student:
    college="Luminar"
    def setval(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        print("Name:", self.name)
        print("Rollno:", self.rollno)
        print("Department", self.dep)
        print("Colllege", Student.college)
    def __str__(self):
        return str(self.rollno)+self.name
std=Student()
std.setval("sree",1,"mca")
print(std)