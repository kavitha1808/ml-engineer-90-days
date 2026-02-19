import numpy as np

data = np.array([
    [50000, 720, 20000],
    [25000, 580, 15000],
    [60000, 650, 40000],
    [28000, 590, 20000]
])

income = data[:, 0]
credit = data[:, 1]
loan = data[:, 2]

risk = (income < 30000) | (credit < 600) | (loan > 0.5 * income)

print("Risky Applicants Index:", np.where(risk)[0])
