class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit):
        self.balance += deposit
        return self.balance
    
    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

acct = BankAccount('Darcy')
print(acct.owner)
print(acct.balance)
acct.deposit(10.0)
acct.withdraw(3)
print(acct.balance)
