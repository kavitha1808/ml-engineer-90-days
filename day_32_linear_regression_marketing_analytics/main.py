import pandas as pd
import matplotlib.pyplot as plt

from src.linear_regression import LinearRegressionGD

# Load dataset
df = pd.read_csv("data/marketing_spend.csv")

X = df["marketing_budget"].values
y = df["customer_spending"].values

# Train model
model = LinearRegressionGD()

model.fit(X, y)

# Predictions
predictions = model.predict(X)

# Plot results
plt.scatter(X, y)
plt.plot(X, predictions)

plt.xlabel("Marketing Budget")
plt.ylabel("Customer Spending")
plt.title("Linear Regression - Marketing Analytics")

plt.savefig("outputs/regression_plot.png")

plt.show()
