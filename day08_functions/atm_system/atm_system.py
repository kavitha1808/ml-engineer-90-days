balance = 5000
pin = 1234

def verify_pin(entered_pin):
    return entered_pin == pin

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Collect your cash")
    else:
        print("Insufficient balance")

def show_balance():
    print("Balance:", balance)

entered_pin = int(input("Enter PIN: "))

if verify_pin(entered_pin):
    withdraw(2000)
    show_balance()
else:
    print("Invalid PIN")
