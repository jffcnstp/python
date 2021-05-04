class User:
    def __init__(self,name,initdeposit=0,initinterest=.1):
        self.username=name
        self.bankbalance=BankAccount(initinterest,initdeposit)

    def make_deposit(self,amount):
        self.bankbalance.deposit(amount)
        return self
    def make_withdrawal(self,amount):
        self.bankbalance.withdraw(amount)
        return self
    def display_user_balance(self):
        print("User: ",self.username)
        self.bankbalance.display_account_info()
        return self
    def transfer_money(self,other_user,amount):
        self.bankbalance.withdraw(amount)
        other_user.bankbalance.deposit(amount)

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


Me=User("Jeff")

Me.display_user_balance().make_deposit(500).display_user_balance().make_withdrawal(100).display_user_balance()

