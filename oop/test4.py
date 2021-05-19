class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def printval(self):
        print("name:",self.name)
        print("age:",self.type)
class Dog(Animal):
    def __init__(self,name,type,age):
        super().__init__(name,type)
        self.age=age
    def print(self):
        print("age:",self.age)
cr=Dog("mill","abc",10)
cr.printval()
cr.print()