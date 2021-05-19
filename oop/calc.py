class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1)
        print(self.num2)
    def add(self):
        print("Addition:",self.num1+self.num2)
    def sub(self):
        print("Substraction:", self.num1-self.num2)
    def mul(self):
        print("Multiplication:",self.num1*self.num2)
    def div(self):
        print("Division:",self.num1/self.num2)
calc=Calculator(15,5)
choice=int(input("Enter 1.add,2.sub,3.mul,4.div"))
if choice==1:
    calc.add()
elif choice==2:
    calc.sub()
elif choice==3:
    calc.mul()
elif choice==4:
    calc.div()
else:
    print("invalid input")