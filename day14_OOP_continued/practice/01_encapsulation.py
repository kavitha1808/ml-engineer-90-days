class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Kavitha", 5000)
acc.deposit(2000)
acc.withdraw(1500)
print("Current Balance:", acc.get_balance())
