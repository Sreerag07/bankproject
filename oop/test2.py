class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Child(Person):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
class Parent(Person):
    def det(self,name,age):
        self.name=name
        self.age=age
class Student(Child):
    def printval(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)
st=Student()
st.details("sree",23)
st.info("sdk","ksd")