class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print(self.num1+self.num2)
add1=Addition()
add1.add(12,32)
add1.printval()