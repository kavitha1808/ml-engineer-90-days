import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score


# ---------------------------------------------------
# 1. Create synthetic dataset
# ---------------------------------------------------
X, y = make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    n_repeated=0,
    n_classes=2,
    random_state=42
)

feature_names = [
    "Feature_1",
    "Feature_2",
    "Feature_3",
    "Feature_4",
    "Feature_5",
    "Feature_6"
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------------------------------------------------
# 2. Random Forest - Built-in Feature Importance
# ---------------------------------------------------
rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)

rf_importances = rf_model.feature_importances_

sorted_idx_rf = np.argsort(rf_importances)[::-1]
sorted_features_rf = [feature_names[i] for i in sorted_idx_rf]
sorted_importances_rf = rf_importances[sorted_idx_rf]

plt.figure(figsize=(10, 6))
plt.bar(sorted_features_rf, sorted_importances_rf)
plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("random_forest_feature_importance.png")
plt.show()


# ---------------------------------------------------
# 3. Logistic Regression - Coefficient Importance
# ---------------------------------------------------
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_pred)

lr_coefficients = np.abs(lr_model.coef_[0])

sorted_idx_lr = np.argsort(lr_coefficients)[::-1]
sorted_features_lr = [feature_names[i] for i in sorted_idx_lr]
sorted_coefficients_lr = lr_coefficients[sorted_idx_lr]

plt.figure(figsize=(10, 6))
plt.bar(sorted_features_lr, sorted_coefficients_lr)
plt.title("Logistic Regression Coefficient Importance (Absolute Values)")
plt.xlabel("Features")
plt.ylabel("Absolute Coefficient Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("logistic_regression_coefficients.png")
plt.show()


# ---------------------------------------------------
# 4. Permutation Importance (using Random Forest)
# ---------------------------------------------------
perm_result = permutation_importance(
    rf_model,
    X_test,
    y_test,
    n_repeats=10,
    random_state=42,
    scoring="accuracy"
)

perm_importances = perm_result.importances_mean

sorted_idx_perm = np.argsort(perm_importances)[::-1]
sorted_features_perm = [feature_names[i] for i in sorted_idx_perm]
sorted_importances_perm = perm_importances[sorted_idx_perm]

plt.figure(figsize=(10, 6))
plt.bar(sorted_features_perm, sorted_importances_perm)
plt.title("Permutation Importance (Random Forest)")
plt.xlabel("Features")
plt.ylabel("Mean Importance Drop")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("permutation_importance.png")
plt.show()


# ---------------------------------------------------
# 5. Print Results
# ---------------------------------------------------
print("========== MODEL PERFORMANCE ==========")
print(f"Random Forest Accuracy      : {rf_accuracy:.4f}")
print(f"Logistic Regression Accuracy: {lr_accuracy:.4f}")

print("\n========== RANDOM FOREST FEATURE IMPORTANCE ==========")
for idx in sorted_idx_rf:
    print(f"{feature_names[idx]}: {rf_importances[idx]:.4f}")

print("\n========== LOGISTIC REGRESSION COEFFICIENT IMPORTANCE ==========")
for idx in sorted_idx_lr:
    print(f"{feature_names[idx]}: {lr_coefficients[idx]:.4f}")

print("\n========== PERMUTATION IMPORTANCE (RANDOM FOREST) ==========")
for idx in sorted_idx_perm:
    print(f"{feature_names[idx]}: {perm_importances[idx]:.4f}")


# ---------------------------------------------------
# 6. Basic Interpretability Notes
# ---------------------------------------------------
print("\n========== MODEL INTERPRETABILITY BASICS ==========")
print("1. Random Forest gives built-in feature importance scores.")
print("2. Logistic Regression uses coefficients to show feature influence.")
print("3. Permutation importance measures how much accuracy drops when a feature is shuffled.")
print("4. Higher importance means the model depends more on that feature.")
print("5. Feature importance helps in understanding, debugging, and feature selection.")
