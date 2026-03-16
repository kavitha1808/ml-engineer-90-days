# Day 42 - Overfitting, Underfitting & Bias-Variance Tradeoff

## Overview
This project demonstrates three important machine learning concepts:

- **Underfitting**
- **Overfitting**
- **Bias–Variance Tradeoff**

Using polynomial regression on a synthetic dataset, we compare simple, balanced, and highly complex models.

---

## Concepts Covered

### 1. Underfitting
A model is too simple and cannot capture the actual pattern in data.

- High bias
- Poor performance on training and testing data

### 2. Good Fit
A balanced model that captures the important patterns without learning noise.

- Good training performance
- Good testing performance

### 3. Overfitting
A model is too complex and learns noise from the training data.

- Very low training error
- High testing error
- High variance

### 4. Bias–Variance Tradeoff
As model complexity increases:

- **Bias decreases**
- **Variance increases**

The goal is to find the right balance where the model generalizes well on unseen data.

---

## Files in this Project

- `day42_overfitting_underfitting_bias_variance.py` → Main Python script
- `outputs/overfitting_underfitting.png` → Visualization of underfitting, good fit, and overfitting
- `outputs/bias_variance_tradeoff.png` → Training vs testing error across model complexity

---

## Libraries Used

- NumPy
- Matplotlib
- Scikit-learn

Install them using:

```bash
pip install numpy matplotlib scikit-learn
```

## How It Works
    - Generate a noisy sine-wave dataset
    - Split data into training and testing sets
    - Train polynomial regression models with different degrees:
       Degree 1 → Underfitting
       Degree 4 → Good Fit
       Degree 15 → Overfitting
    - Compare training and testing errors
    - Plot training and testing error curves to visualize the bias–variance tradeoff
--- 

## Expected Output

1. Model Fit Comparison
     - Shows three graphs:
     - Underfitting model
     - Good fit model
     - Overfitting model
Saved as:
outputs/overfitting_underfitting.png

2. Bias–Variance Tradeoff Curve
Shows:
- Training error decreases as complexity increases
- Testing error first decreases, then increases
Saved as:
outputs/bias_variance_tradeoff.png






