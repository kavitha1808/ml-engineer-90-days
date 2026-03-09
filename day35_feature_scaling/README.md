# Day 35 – Feature Scaling

## Normalization vs Standardization

Feature scaling is a preprocessing technique used in Machine Learning to bring different features into the same scale. Many algorithms such as KNN, SVM, Neural Networks and Gradient Descent work better when features are scaled.

This project demonstrates two common scaling techniques:

- Normalization (Min-Max Scaling)
- Standardization (Z-score Scaling)

---

# Dataset

Sample dataset used:

| Age | Salary |
|----|----|
|20|20000|
|25|30000|
|30|40000|
|35|50000|
|40|60000|

---

# 1 Normalization

Normalization rescales values between **0 and 1**.

Formula:

X_norm = (X − X_min) / (X_max − X_min)

Advantages

- Works well for neural networks
- Keeps values within a fixed range
- Useful for image processing

Disadvantages

- Sensitive to outliers

---

# 2 Standardization

Standardization transforms data to have:

- Mean = 0
- Standard Deviation = 1

Formula:

X_std = (X − μ) / σ

Advantages

- Handles outliers better
- Preferred for many ML algorithms
- Works well for linear models

Disadvantages

- Values are not bounded

---

# Comparison

| Feature | Normalization | Standardization |
|------|------|------|
| Formula | (X − min)/(max − min) | (X − μ)/σ |
| Range | 0 to 1 | No fixed range |
| Outliers | Sensitive | More robust |
| Best Use | Neural networks | Linear models |

---

# Visualization

The project visualizes the difference between:

- Original data
- Normalized data
- Standardized data

Output plot:

```

outputs/scaling_visualization.png

```

---

# Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

# Conclusion

Feature scaling improves machine learning model performance by ensuring all features contribute equally to training.

Normalization is useful when data must lie in a specific range, while Standardization is preferred for algorithms assuming normally distributed data.

---

Part of my **90 Day Machine Learning Engineer Roadmap**
