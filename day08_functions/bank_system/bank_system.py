balance = 1000

def check_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawn:", amount)

check_balance()
deposit(500)
withdraw(300)
withdraw(2000)
check_balance()
