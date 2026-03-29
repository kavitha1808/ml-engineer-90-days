# Day 55 - Error Analysis & Debugging ML Models

import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# 1. Load Dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print("Dataset Loaded Successfully\n")

# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 4. Predictions
y_pred = model.predict(X_test)

# 5. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# 6. Error Analysis
print("\n--- Error Analysis ---\n")

wrong_predictions = X_test[y_test != y_pred]
wrong_actual = y_test[y_test != y_pred]
wrong_predicted = y_pred[y_test != y_pred]

error_df = wrong_predictions.copy()
error_df["Actual"] = wrong_actual.values
error_df["Predicted"] = wrong_predicted

print("Misclassified Samples:\n")
print(error_df)

# 7. Feature Insight (Simple Analysis)
print("\n--- Feature Summary of Errors ---\n")
print(error_df.describe())

# 8. Class Distribution Check
print("\n--- Class Distribution ---\n")
print(y.value_counts())

# 9. Conclusion Print
print("\nModel Debugging Completed.")
