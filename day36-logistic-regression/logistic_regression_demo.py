# Day 36 - Logistic Regression (Classification)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample dataset (Hours studied vs Pass/Fail)
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([0,0,0,0,1,1,1,1])   # 0 = Fail, 1 = Pass

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)

print("Predictions:", predictions)
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)

# Visualization
plt.scatter(X, y)

# Logistic curve
x_values = np.linspace(0,10,100).reshape(-1,1)
y_prob = model.predict_proba(x_values)[:,1]

plt.plot(x_values, y_prob)

plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression Classification Curve")

plt.savefig("logistic_regression_visualization.png")
plt.show()
