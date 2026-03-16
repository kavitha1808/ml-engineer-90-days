import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create output folder
os.makedirs("outputs", exist_ok=True)


# Generate synthetic dataset

np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.2, size=100)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Degrees for underfit, good fit, overfit
degrees = [1, 4, 15]
titles = ["Underfitting (Degree=1)", "Good Fit (Degree=4)", "Overfitting (Degree=15)"]

# Smooth curve for plotting
X_plot = np.linspace(0, 10, 300).reshape(-1, 1)

# Store errors
train_errors = []
test_errors = []


plt.figure(figsize=(15, 4))

for i, degree in enumerate(degrees):
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    y_plot = model.predict(X_plot)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    train_errors.append(train_mse)
    test_errors.append(test_mse)

    plt.subplot(1, 3, i + 1)
    plt.scatter(X_train, y_train, label="Train Data", alpha=0.7)
    plt.scatter(X_test, y_test, label="Test Data", alpha=0.7)
    plt.plot(X_plot, y_plot, linewidth=2, label=f"Degree {degree}")
    plt.title(f"{titles[i]}\nTrain MSE={train_mse:.3f}, Test MSE={test_mse:.3f}")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()

plt.tight_layout()
plt.savefig("outputs/overfitting_underfitting.png")
plt.show()

degree_range = range(1, 16)
all_train_errors = []
all_test_errors = []

for degree in degree_range:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    all_train_errors.append(mean_squared_error(y_train, y_train_pred))
    all_test_errors.append(mean_squared_error(y_test, y_test_pred))

plt.figure(figsize=(8, 5))
plt.plot(degree_range, all_train_errors, marker='o', label="Training Error")
plt.plot(degree_range, all_test_errors, marker='s', label="Testing Error")
plt.xlabel("Polynomial Degree (Model Complexity)")
plt.ylabel("Mean Squared Error")
plt.title("Bias-Variance Tradeoff")
plt.legend()
plt.grid(True)
plt.savefig("outputs/bias_variance_tradeoff.png")
plt.show()

print("Day 42 - Overfitting, Underfitting & Bias-Variance Tradeoff")
print("-" * 55)
for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    print(f"Degree {degree}: Train MSE = {train_mse:.4f}, Test MSE = {test_mse:.4f}")
