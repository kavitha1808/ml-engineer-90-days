import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve
)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=5000),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC(probability=True, random_state=42)
}

# Store results
results = []

# Plot ROC curves
plt.figure(figsize=(10, 6))

for name, model in models.items():
    # Use scaled data for all models for fair comparison
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    results.append([name, acc, prec, rec, f1, roc_auc])

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.2f})")

# ROC plot formatting
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison of Classification Models")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/model_roc_comparison.png")
plt.close()

# Create results DataFrame
results_df = pd.DataFrame(
    results,
    columns=["Model", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
)

# Print results
print("\nClassification Model Comparison Results:\n")
print(results_df)

# Plot comparison bar chart (using F1 Score)
plt.figure(figsize=(10, 6))
plt.bar(results_df["Model"], results_df["F1 Score"])
plt.xlabel("Model")
plt.ylabel("F1 Score")
plt.title("F1 Score Comparison of Classification Models")
plt.xticks(rotation=15)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("outputs/model_comparison_bar_chart.png")
plt.close()

print("\nPlots saved successfully:")
print("1. outputs/model_comparison_bar_chart.png")
print("2. outputs/model_roc_comparison.png")
