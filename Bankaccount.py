class BankAccount:
    def __init__(self, int_rate,balance):
        self.interest=int_rate
        self.currbal=balance

    def deposit(self,amount):
        self.currbal+=amount
        return self
    def withdraw(self, amount):
        self.currbal-=amount
        return self

    def display_account_info(self):
        print("Interest Rate: ",self.interest)
        print("Current Balance: ",self.currbal)
        return self

    def yield_interest(self):
        if(self.currbal<0):
            print("PAY YOUR DEBT YOU LAZY LAD")
            return self
        else:
            self.currbal=self.currbal+(self.currbal*self.interest)
            return self


MyAccount=BankAccount(.09,300)
YourAccount=BankAccount(.12,4000)

MyAccount.deposit(300).deposit(300).deposit(23).withdraw(400).yield_interest().display_account_info()

YourAccount.deposit(20).deposit(40).withdraw(1000).withdraw(1000).withdraw(2000).withdraw(3000).yield_interest().display_account_info()
