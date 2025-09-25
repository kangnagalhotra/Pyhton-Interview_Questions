# Create a class that hides a variable (encapsulation).

class bankaccount:
    def __init__(self , balance=0):
        self.balance =  balance
    def deposit(self, amount):
        self.amount = amount
        if amount > 0:
            self.balance += amount   
        else:
            print("Deposit must be positive")
    def withdraw(self,amount):
        if amount>0 and amount <= self.balance:
            self.balance-=amount
    def get_Balance(self):
        return self.balance
    
account = bankaccount(1000)
account.deposit(500)
print(account.get_Balance())
account.withdraw(100)
print(account.get_Balance())

        
            