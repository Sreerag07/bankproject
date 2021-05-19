class Student:
    college="sridevi"
    def __init__(self,name,rollno,age):
        self.name=name
        self.age=age
        self.rollno=rollno
    def printval(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Age:",self.age)
        print("College:",Student.college)
obj=Student("sree",1234,24)
obj.printval()