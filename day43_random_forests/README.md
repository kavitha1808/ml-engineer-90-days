# Day 43 - Random Forests & Ensemble Learning

## Objective
This project demonstrates the implementation of **Random Forests** and the concept of **Ensemble Learning** using:
- **Random Forest Classification**
- **Random Forest Regression**
- **Feature Importance Visualization**

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve accuracy and reduce overfitting.

---

## Concepts Covered

### 1. Ensemble Learning
Ensemble learning is a machine learning technique where multiple models are combined to make better predictions than a single model.

### 2. Random Forest
Random Forest is an ensemble method based on:
- **Bagging (Bootstrap Aggregating)**
- **Random Feature Selection**

It builds multiple decision trees and combines their predictions.

- **Classification** → Majority Voting
- **Regression** → Average Prediction

### 3. Feature Importance
Random Forest can estimate which features are most important for making predictions.

---

## Project Files

- `random_forest_day43.py` → Main Python script
- `outputs/random_forest_classification_boundary.png` → Classification decision boundary
- `outputs/random_forest_regression_plot.png` → Regression prediction plot
- `outputs/random_forest_feature_importance.png` → Feature importance chart

---

## Libraries Used

- `numpy`
- `matplotlib`
- `scikit-learn`
- `os`

---

## What This Project Does

### Part 1: Random Forest Classification
- Creates a synthetic classification dataset
- Trains a `RandomForestClassifier`
- Evaluates accuracy and classification report
- Visualizes the decision boundary

### Part 2: Random Forest Regression
- Creates a synthetic regression dataset
- Trains a `RandomForestRegressor`
- Evaluates using:
  - Mean Squared Error (MSE)
  - R² Score
- Visualizes the regression prediction curve

### Part 3: Feature Importance
- Trains a Random Forest on a multi-feature dataset
- Extracts feature importance values
- Plots feature importance using a bar chart

---

## Sample Output (Console)

```bash
============================================================
RANDOM FOREST CLASSIFICATION
============================================================
Classification Accuracy: 0.9500

Classification Report:
              precision    recall  f1-score   support
           0       0.95      0.94      0.95        XX
           1       0.95      0.96      0.95        XX

============================================================
RANDOM FOREST REGRESSION
============================================================
Regression Mean Squared Error: XXXX.XXXX
Regression R2 Score: 0.8XXX

============================================================
FEATURE IMPORTANCE
============================================================
Feature 1: 0.12XX
Feature 2: 0.25XX
Feature 3: 0.18XX
Feature 4: 0.21XX
Feature 5: 0.10XX
Feature 6: 0.13XX
```

---
## Learning Outcomes
 - By completing this project, I learned:
 - How Ensemble Learning improves model performance
 - The  difference between a single Decision Tree and Random Forest
 - How Random Forest reduces overfitting and variance
 - How to use:
 - RandomForestClassifier
 - RandomForestRegressor
 - How to evaluate classification and regression models
 - How to visualize:
 - decision boundaries
 - regression predictions
 - feature importance
