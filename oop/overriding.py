class Person:
    def details(self,mode):
        self.mode=mode
        print("The perzon is working on hardware mode",self.mode)
    def salary(self,sal):
        self.sal=sal
        print(self.sal)
class Student(Person):
    def details(self,mode):
        self.mode=mode
        print("The person is working on software mode",self.mode)
st=Student()
st.details(1)
st.salary(50000)