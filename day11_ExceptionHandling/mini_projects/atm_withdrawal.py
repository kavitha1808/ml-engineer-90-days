balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient balance")
    elif amount <= 0:
        raise ValueError
    else:
        balance -= amount
        print("Withdrawn:", amount)
        print("Remaining balance:", balance)

except ValueError:
    print("Invalid amount entered")
