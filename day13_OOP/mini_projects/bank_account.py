class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def get_balance(self):
        return self.balance

    def display_account(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        print("Balance: ₹", self.balance)


# Driver code
acc1 = BankAccount("Kavitha", 5000)
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.display_account()
