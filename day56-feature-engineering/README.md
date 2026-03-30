# Day 56 – Feature Engineering Strategies

## 📌 Overview
Feature Engineering is the process of transforming raw data into meaningful features that improve machine learning model performance.

---

## 🚀 Techniques Implemented

### 1. Handling Missing Values
- Filled missing Age with mean
- Filled missing Salary with median

### 2. Encoding Categorical Variables
- One-hot encoding for City column

### 3. Feature Scaling
- StandardScaler used to normalize Age and Salary

### 4. Feature Creation
- Created new feature: Age_Salary_Ratio

### 5. Binning
- Converted Age into categories (Young, Middle, Old)

### 6. Feature Selection
- Used SelectKBest to select top 3 important features

---

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

---

## ▶️ How to Run
```bash
pip install pandas numpy scikit-learn
python feature_engineering.py

```

## 📊 Output
- Cleaned dataset
- Scaled features
- Selected best features for model training
---

## 💡 Why Feature Engineering Matters
- Improves model accuracy
- Reduces overfitting
- Makes patterns easier to learn
