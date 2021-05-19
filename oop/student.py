#instance variable related to methods
#class variable related to class
class Student:
    college="Luminar"
    def setval(self,name,id):
        self.name=name
        self.id=id
    def printval(self):
        print("Name:",self.name)
        print("Id:",self.id)
        print("Colllege",Student.college)#class variable
st=Student()
st.setval("sree",1234)
st.printval()
st1=Student()
st1.setval("Anu",1234)
st1.printval()