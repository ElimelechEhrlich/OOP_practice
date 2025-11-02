class BankAccount:
    def __init__(self,  account_number,  balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): # → increases balance
        self.amount = amount
        self.balance += amount

    def withdraw(self, amount): #→ decreases balance (only if enough money)
        self.amount = amount
        if self.balance > amount:
            self.balance -= amount

    def get_balance(self): #→ returns the balance
        return f'the balance of account number: {self.account_number} is {self.balance}'

account1 = BankAccount('123456', 500)
print (account1.account_number)
print (account1.get_balance())
account1.deposit(100)
print (account1.get_balance())
account1.withdraw(300)
print (account1.get_balance())



