#class-design patterns
#object-realworld entity
#referrence-name that refers a memory location
# class Person:
#     def walk(self):
#         print("person is walking")
#     def jumb(self):
#         print("person is jumping")
# obj=Person()
# obj.walk()
# obj.jumb()
# obj1=Person()
# obj1.walk()
# obj1.jumb()
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print(self.name)
#         print(self.age)
# obj=Person()
# obj.details("sree",22)
# obj.printval()
class Employee:
    company="Luminar"
    def details(self,name,place,sex,age,salary):
        self.name=name
        self.place=place
        self.sex=sex
        self.age=age
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.place)
        print(self.sex)
        print(self.age)
        print(self.salary)
        print(Employee.company)
obj=Employee()
obj.details("sree","kanhangad","M",22,15000)
obj.printval()










