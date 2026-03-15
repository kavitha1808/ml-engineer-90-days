import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Decision Tree model using Gini criterion
model = DecisionTreeClassifier(
    criterion="gini",   # try "entropy" also
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

# Plot Decision Tree
plt.figure(figsize=(16, 8))
plot_tree(
    model,
    feature_names=feature_names,
    class_names=target_names,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree Classifier (Gini Criterion)")
plt.tight_layout()
plt.savefig("outputs/decision_tree_plot.png")
plt.close()

# Plot Feature Importance
importances = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.bar(feature_names, importances)
plt.xticks(rotation=45)
plt.ylabel("Importance Score")
plt.title("Feature Importance in Decision Tree")
plt.tight_layout()
plt.savefig("outputs/feature_importance.png")
plt.close()

# Compare Gini vs Entropy
gini_model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
entropy_model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)

gini_model.fit(X_train, y_train)
entropy_model.fit(X_train, y_train)

gini_acc = accuracy_score(y_test, gini_model.predict(X_test))
entropy_acc = accuracy_score(y_test, entropy_model.predict(X_test))

print("\n--- Splitting Criteria Comparison ---")
print(f"Gini Accuracy   : {gini_acc:.4f}")
print(f"Entropy Accuracy: {entropy_acc:.4f}")
