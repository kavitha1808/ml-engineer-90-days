class Wallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print("Money added")
        else:
            print("Invalid amount")

    def spend_money(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Money spent")

    def show_balance(self):
        print("Current Balance:", self.balance)


wallet = Wallet()

while True:
    print("\n1. Add Money")
    print("2. Spend Money")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = int(input("Enter amount: "))
        wallet.add_money(amt)

    elif choice == "2":
        amt = int(input("Enter amount: "))
        wallet.spend_money(amt)

    elif choice == "3":
        wallet.show_balance()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
