class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


bank_account = BankAccount()
bank_account.deposit(1175)
bank_account.withdraw(25)
print("Balance:", bank_account.balance)
