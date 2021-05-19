class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:", self.name)
        print("age:", self.age)
class Employee(Person):
    def __init__(self,name,age,id,company,salary):
        super().__init__(name,age)
        self.id=id
        self.company=company
        self.salary=salary
    def print(self):
        print("id",self.id)
        print("company",self.company)
        print("salary",self.salary)
emp=Employee("sree",25,12345,"luminar",25000)
emp.printval()
emp.print()