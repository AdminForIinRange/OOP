balance = 0


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    balance -= amount


deposit(1175)
withdraw(25)
print("Balance:", balance)
