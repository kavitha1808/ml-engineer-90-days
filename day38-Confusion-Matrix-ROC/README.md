# Day 38 - Confusion Matrix and ROC Curve

This project demonstrates evaluation metrics used in classification models.

## Topics Covered

- Confusion Matrix
- True Positive, False Positive
- ROC Curve
- AUC Score

## Dataset

Breast Cancer dataset from Scikit-learn.

## Libraries Used

- numpy
- matplotlib
- scikit-learn

Install dependencies:

pip install numpy matplotlib scikit-learn

## How to Run

Run the python file:

python confusion_matrix_roc.py

## Output

The program generates:

confusion_matrix.png  
roc_curve.png

## Confusion Matrix

A confusion matrix evaluates classification performance by showing:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

## ROC Curve

ROC curve shows the performance of a classification model at different thresholds.

- X axis → False Positive Rate
- Y axis → True Positive Rate

## AUC Score

AUC (Area Under Curve) measures how well the model separates classes.

- AUC = 1 → Perfect model
- AUC = 0.5 → Random guessing
