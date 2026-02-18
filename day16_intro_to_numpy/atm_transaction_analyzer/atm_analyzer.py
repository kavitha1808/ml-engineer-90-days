import numpy as np
from sample_data import transactions

print("ATM Transactions:", transactions)

# Total and average
total = np.sum(transactions)
average = np.mean(transactions)

# Risk analysis
high_value = transactions[transactions > 10000]
fraud_alert = transactions[transactions > 20000]

print("\nTotal Withdrawn:", total)
print("Average Withdrawal:", average)
print("High Value Withdrawals:", high_value)
print("⚠️ Fraud Alert Transactions:", fraud_alert)
