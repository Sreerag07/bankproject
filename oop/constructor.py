#used to initialize instance variable
#constructor automatically invoke when creating an object
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
obj=Person("sree",23,"male")
obj.printval()