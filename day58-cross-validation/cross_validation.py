# cross_validation.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Model
model = LogisticRegression(max_iter=200)

# -------------------------------
# 1. Simple Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

print("Train-Test Accuracy:", accuracy)

# -------------------------------
# 2. Cross Validation (K-Fold)
# -------------------------------
scores = cross_val_score(model, X, y, cv=5)

print("Cross-Validation Scores:", scores)
print("Average Accuracy:", scores.mean())

# -------------------------------
# 3. Manual K-Fold
# -------------------------------
kf = KFold(n_splits=5, shuffle=True)

manual_scores = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    manual_scores.append(score)

print("Manual K-Fold Scores:", manual_scores)
print("Manual Average Accuracy:", sum(manual_scores)/len(manual_scores))
