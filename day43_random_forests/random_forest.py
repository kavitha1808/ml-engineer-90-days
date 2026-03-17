import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# PART 1: RANDOM FOREST CLASSIFICATION


print("=" * 60)
print("RANDOM FOREST CLASSIFICATION")
print("=" * 60)

# Create a synthetic classification dataset
X_class, y_class = make_classification(
    n_samples=500,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=42
)

# Split data
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42
)

# Train Random Forest Classifier
rf_clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
rf_clf.fit(Xc_train, yc_train)

# Predictions
yc_pred = rf_clf.predict(Xc_test)

# Metrics
clf_acc = accuracy_score(yc_test, yc_pred)
print(f"Classification Accuracy: {clf_acc:.4f}")
print("\nClassification Report:")
print(classification_report(yc_test, yc_pred))

# Plot decision boundary
x_min, x_max = X_class[:, 0].min() - 1, X_class[:, 0].max() + 1
y_min, y_max = X_class[:, 1].min() - 1, X_class[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.02),
    np.arange(y_min, y_max, 0.02)
)

Z = rf_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X_class[:, 0], X_class[:, 1], c=y_class, edgecolors='k', alpha=0.8)
plt.title("Random Forest Classification Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.savefig("outputs/random_forest_classification_boundary.png")
plt.close()


# PART 2: RANDOM FOREST REGRESSION

print("=" * 60)
print("RANDOM FOREST REGRESSION")
print("=" * 60)

# Create a synthetic regression dataset
X_reg, y_reg = make_regression(
    n_samples=300,
    n_features=1,
    noise=20,
    random_state=42
)

# Sort for smooth plotting
sorted_idx = np.argsort(X_reg[:, 0])
X_reg = X_reg[sorted_idx]
y_reg = y_reg[sorted_idx]

# Split data
Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# Train Random Forest Regressor
rf_reg = RandomForestRegressor(
    n_estimators=100,
    max_depth=6,
    random_state=42
)
rf_reg.fit(Xr_train, yr_train)

# Predictions
yr_pred = rf_reg.predict(Xr_test)

# Metrics
mse = mean_squared_error(yr_test, yr_pred)
r2 = r2_score(yr_test, yr_pred)

print(f"Regression Mean Squared Error: {mse:.4f}")
print(f"Regression R2 Score: {r2:.4f}")

# Smooth line prediction for plot
X_line = np.linspace(X_reg.min(), X_reg.max(), 500).reshape(-1, 1)
y_line_pred = rf_reg.predict(X_line)

plt.figure(figsize=(8, 6))
plt.scatter(X_reg, y_reg, alpha=0.6, label="Actual Data")
plt.plot(X_line, y_line_pred, linewidth=2, label="Random Forest Prediction")
plt.title("Random Forest Regression")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.savefig("outputs/random_forest_regression_plot.png")
plt.close()

# PART 3: FEATURE IMPORTANCE

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

# Create a multi-feature dataset for feature importance
X_feat, y_feat = make_classification(
    n_samples=500,
    n_features=6,
    n_informative=4,
    n_redundant=0,
    random_state=42
)

feature_names = [f"Feature {i+1}" for i in range(X_feat.shape[1])]

rf_feat = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_feat.fit(X_feat, y_feat)

importances = rf_feat.feature_importances_

# Print feature importance values
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

# Plot feature importance
plt.figure(figsize=(8, 6))
plt.bar(feature_names, importances)
plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/random_forest_feature_importance.png")
plt.close()


# FINAL MESSAGE

print("=" * 60)
print("All outputs saved successfully in 'outputs/' folder")
print("1. random_forest_classification_boundary.png")
print("2. random_forest_regression_plot.png")
print("3. random_forest_feature_importance.png")
print("=" * 60)
