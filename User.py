class User:
    def __init__(self,name,initdeposit):
        self.username=name
        self.bankbalance=initdeposit
    def make_deposit(self,amount):
        self.bankbalance+=amount
    def make_withdrawal(self,amount):
        self.bankbalance-=amount
    def display_user_balance(self):
        print("User: ",self.username)
        print("Current Balance: ", self.bankbalance)
    def transfer_money(self,other_user,amount):
        self.bankbalance-=amount
        other_user.bankbalance+=amount

Me=User("Jeff",100)
Plebian=User("Poorman",0)
God=User("Richman",2000)

Me.make_deposit(100)
Me.make_deposit(150)
Me.make_withdrawal(130)
Me.display_user_balance()

Plebian.make_deposit(1)
Plebian.make_deposit(2)
Plebian.make_withdrawal(1)
Plebian.make_withdrawal(4)
Plebian.display_user_balance()

God.make_deposit(6000)
God.make_withdrawal(1500)
God.make_withdrawal(1500)
God.make_withdrawal(10)
God.display_user_balance()

God.transfer_money(Me,2000)
God.display_user_balance()
Me.display_user_balance()

