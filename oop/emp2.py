class Employee:
    company="Luminar"
    def addval(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.salary)
        print(Employee.company)
    def __str__(self):
        return self.name+ str(self.age)+str(self.salary)     #this class only accept the string values
emp=Employee()
emp.addval("sree",23,12345,250000)
emp.printval()
print(emp)