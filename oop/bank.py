class Bank:
    bname="Syn bank"
    def account(self,name,accno):
        self.name=name
        self.accno=accno
        self.minimumbal=5000
        self.balance=self.minimumbal
        print("your", Bank.bname, "account has been created with", self.minimumbal)
    def deposite(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("your",Bank.bname,"account has been credited with",self.amt)
        print("your current balance is",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            print("account is debited with",self.amnt)
            self.balance-=self.amnt
            print("available balance is:",self.balance)
acc=Bank()
acc.account("sree",12345)
acc.deposite(2500)
acc.withdraw(1000)