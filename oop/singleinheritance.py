class Person:                   #Super class,Base class,Parent class
    def addval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):          #Derived class,Sub class,Child class
    def printval(self,id,name,company,salary):
        self.id=id
        self.name=name
        self.company=company
        self.salary=salary
        print(self.id)
        print(self.name)
        print(self.company)
        print(self.salary)
obj=Person()
obj.addval("sree",23,"Male")
obj1=Employee()
obj1.printval(123,"athira","Luminar",50000)
obj1.addval("anu",25,"female")
