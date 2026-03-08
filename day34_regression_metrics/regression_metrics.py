# Day 34 - Regression Evaluation Metrics
# MAE, MSE, RMSE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Example dataset (House price prediction)
y_true = np.array([200, 250, 300, 350, 400])
y_pred = np.array([210, 240, 310, 330, 390])

# Calculate metrics
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

print("Actual Values:", y_true)
print("Predicted Values:", y_pred)

print("\nEvaluation Metrics")
print("-------------------")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)

# Visualization
plt.figure(figsize=(8,5))
plt.plot(y_true, marker='o', label="Actual Prices")
plt.plot(y_pred, marker='s', label="Predicted Prices")

plt.title("Actual vs Predicted House Prices")
plt.xlabel("House Index")
plt.ylabel("Price")
plt.legend()

plt.savefig("outputs/error_visualization.png")
plt.show()
