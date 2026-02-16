class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def deposit(self, amount):
        self._balance += amount


class LoanAccount(Account):
    def __init__(self, loan_amount, interest):
        super().__init__(loan_amount)
        self.interest = interest

    def calculate_emi(self, months):
        return (self._balance * (1 + self.interest)) / months

    def pay_emi(self, amount):
        self._balance -= amount


loan = LoanAccount(50000, 0.1)
print("EMI:", loan.calculate_emi(10))
