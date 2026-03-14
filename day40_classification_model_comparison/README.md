# Day 40 - Classification Model Comparison

## Overview
This project compares multiple classification models on the Breast Cancer dataset using common evaluation metrics.  
The goal is to understand how to choose the best classification model based on performance metrics rather than relying only on accuracy.

## Models Compared
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

## Dataset
- Breast Cancer Dataset from scikit-learn

## Concepts Covered
- Train-test split
- Feature scaling
- Training multiple classification models
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC-AUC
- ROC curve comparison
- Bar chart comparison of model performance

## Files
- `classification_model_comparison.py` → Main Python script
- `outputs/model_comparison_bar_chart.png` → F1 score comparison bar chart
- `outputs/model_roc_comparison.png` → ROC curve comparison plot

## Output
The script:
1. Loads the Breast Cancer dataset
2. Splits data into training and testing sets
3. Applies feature scaling
4. Trains 5 classification models
5. Evaluates them using multiple metrics
6. Prints a comparison table
7. Saves:
   - F1 Score comparison bar chart
   - ROC curve comparison plot

## Example Metrics Used
- **Accuracy** → Overall correct predictions
- **Precision** → Correct positive predictions out of all predicted positives
- **Recall** → Correct positive predictions out of all actual positives
- **F1 Score** → Balance between precision and recall
- **ROC-AUC** → Ability of the model to separate classes

## How to Run
```bash
python classification_model_comparison.py
