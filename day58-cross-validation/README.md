# Day 58 – Cross Validation

## 📌 What is Cross Validation?

Cross-validation is a technique used to evaluate machine learning models by training and testing multiple times on different subsets of data.

It helps to:
- Reduce overfitting
- Give better accuracy estimation
- Use data efficiently

---

## 🔁 K-Fold Cross Validation

- Split dataset into K folds
- Train on K-1 folds
- Test on remaining fold
- Repeat K times
- Take average score

Example: K = 5

---

## ⚙️ Methods Used

### 1. Train-Test Split
Basic method where data is split once.

### 2. cross_val_score()
Built-in sklearn method for cross-validation.

### 3. KFold
Manual control over splitting.

---

## 📊 Output Example
Train-Test Accuracy: 0.96 Cross-Validation Scores: [0.96 1.00 0.93 0.96 1.00] Average Accuracy: 0.97

---

## 🚀 Key Benefits

- Better model evaluation
- Less bias compared to single split
- Works well for small datasets

---

## 🧠 When to Use?

- Small datasets
- Model comparison
- Hyperparameter tuning

---

## 📁 Files

- cross_validation.py

---

## 🛠️ Requirements
```
pip install scikit-learn
```
---

## ▶️ Run
```
python cross_validation.py
```
