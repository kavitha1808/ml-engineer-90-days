import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# -----------------------------
# 1. Load Dataset
# -----------------------------

df = pd.read_csv("data/house_prices.csv")

print("Dataset Preview:")
print(df.head())


# -----------------------------
# 2. Define Features and Target
# -----------------------------

X = df[["size_sqft", "bedrooms", "house_age"]]
y = df["price"]


# -----------------------------
# 3. Train-Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -----------------------------
# 4. Train Machine Learning Model
# -----------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# -----------------------------
# 5. Make Predictions
# -----------------------------

predictions = model.predict(X_test)


# -----------------------------
# 6. Evaluate Model
# -----------------------------

mae = mean_absolute_error(y_test, predictions)

print("\nModel Evaluation")
print("Mean Absolute Error:", mae)


# -----------------------------
# 7. Save Predictions
# -----------------------------

results = X_test.copy()
results["Actual Price"] = y_test
results["Predicted Price"] = predictions

results.to_csv("outputs/prediction_results.csv", index=False)

print("\nPredictions saved to outputs/prediction_results.csv")
