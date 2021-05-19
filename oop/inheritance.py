#called single inheritance because derive from one base class by one sub class
class Person:                   #Super class,Base class,Parent class
    def addval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):          #Derived class,Sub class,Child class
    def printval(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)
obj=Person()
obj.addval("sree",23,"male")
st=Student()
st.printval("cs","sridevi")
st.addval("anu",22,"male")