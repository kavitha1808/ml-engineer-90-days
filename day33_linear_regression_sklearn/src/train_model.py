import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/marketing_sales.csv")

# Features and target
X = df[["marketing_budget"]]
y = df["sales"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Plot regression line
plt.scatter(X, y)

plt.plot(
    X,
    model.predict(X),
)

plt.xlabel("Marketing Budget")
plt.ylabel("Sales")
plt.title("Marketing Budget vs Sales Prediction")

plt.savefig("outputs/regression_plot.png")

plt.show()
