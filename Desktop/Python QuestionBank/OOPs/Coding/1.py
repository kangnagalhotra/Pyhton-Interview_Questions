# Create a class BankAccount with deposit & withdraw methods.

class BankAccount:
    def __init__(self,balance=0):
        self.balance =  balance
    def deposit(self , amount):
        if amount>0:
            self.balance+=amount
            print("New Balance: " , {self.balance})
        else:
            print("Deposite should be positive")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print("New Balance: " ,{self.balance})
        else:
            print("Withdraw amount is more than balance")
account = BankAccount(1000)
account.deposit(600)
account.withdraw(100)

        
    
    
    