#polymorphism-many forms
#Overriding-same method name different signatures\
#overriding-Same method name same parameters
#python support overriding(child class methos will be overridden

#1.OVERLOADING
# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2+self.num3)
# st=Student()
# st.show(5,6)

#2.OVERRIDING
class Parent:
    def properties(self):
        print("inside prop")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()