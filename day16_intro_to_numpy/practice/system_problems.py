import numpy as np

# Problem 5: ATM Withdrawal Analysis
withdrawals = np.array([2000, 5000, 10000, 2000, 25000, 3000])

print("ATM Total Withdrawal:", np.sum(withdrawals))
print("ATM Average Withdrawal:", np.mean(withdrawals))
print("Withdrawals > 8000:", np.sum(withdrawals > 8000))
print("Suspicious Withdrawals:", withdrawals[withdrawals > 15000])

# Problem 6: Temperature Monitoring
temperature = np.array([28, 30, 35, 40, 38, 29, 27])

print("\nMax Temperature:", np.max(temperature))
print("Overheating Values:", temperature[temperature > 37])

fahrenheit = (temperature * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Problem 7: Student Result Processing
marks = np.array([
    [78, 85, 90],
    [60, 72, 68],
    [88, 92, 95]
])

total_per_student = np.sum(marks, axis=1)
avg_per_subject = np.mean(marks, axis=0)
topper_index = np.argmax(total_per_student)

print("\nTotal Marks per Student:", total_per_student)
print("Average Marks per Subject:", avg_per_subject)
print("Topper Student Index:", topper_index)
