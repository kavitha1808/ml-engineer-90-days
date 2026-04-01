# Day 57 – Hyperparameter Tuning

## 📌 What is Hyperparameter Tuning?

Hyperparameters are settings that control how a machine learning model learns.

Examples:
- Learning rate
- Number of trees
- Regularization (C)

Tuning them improves model performance.

---

## 🔍 GridSearchCV

GridSearchCV tries ALL possible combinations of parameters.

### Example:
C = [0.1, 1, 10]
kernel = ['linear', 'rbf']

Total = 3 × 2 = 6 combinations

It:
- Trains model for each combination
- Uses cross-validation
- Picks the best one

---

## ⚡ RandomizedSearchCV

Instead of trying all combinations, it:
- Picks random combinations
- Much faster
- Useful for large datasets

---

## 🆚 Grid vs Random

| Feature          | GridSearchCV | RandomizedSearchCV |
|----------------|-------------|-------------------|
| Speed          | Slow        | Fast              |
| Accuracy       | High        | Good              |
| Use Case       | Small data  | Large data        |

---

## ▶️ How to Run

```bash
python grid_search.py
python random_search.py

```
---
## 🎯 Output Example

Best Parameters: {'C': 10, 'kernel': 'rbf', 'gamma': 'scale'}
Best Score: 0.97

