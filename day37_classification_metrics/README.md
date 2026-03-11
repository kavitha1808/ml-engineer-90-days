# Day 37 - Classification Metrics

This project demonstrates the most important evaluation metrics used in classification problems in Machine Learning.

Metrics Covered:
- Accuracy
- Precision
- Recall
- F1 Score

These metrics help evaluate how well a classification model performs.

-----------------------------------------------------

Dataset

A small sample dataset of true labels and predicted labels is used to demonstrate how metrics are calculated.

Example:

y_true = [1,0,1,1,0,1,0,1,1,0]
y_pred = [1,0,1,0,0,1,0,1,0,0]

-----------------------------------------------------

Metrics Explanation

1. Accuracy

Accuracy measures the overall correctness of the model.

Formula:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Where:
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative

-----------------------------------------------------

2. Precision

Precision measures how many predicted positives are actually positive.

Formula:

Precision = TP / (TP + FP)

High precision means fewer false positives.

-----------------------------------------------------

3. Recall

Recall measures how many actual positives are correctly predicted.

Formula:

Recall = TP / (TP + FN)

High recall means fewer false negatives.

-----------------------------------------------------

4. F1 Score

F1 Score is the harmonic mean of precision and recall.

Formula:

F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

It balances both precision and recall.

-----------------------------------------------------

Visualization

A bar chart is used to compare Accuracy, Precision, Recall, and F1 Score.

-----------------------------------------------------

Libraries Used

- scikit-learn
- matplotlib

Install using:

pip install scikit-learn
pip install matplotlib

-----------------------------------------------------

Output

The program prints:

- Confusion Matrix
- Accuracy
- Precision
- Recall
- F1 Score

And generates a visualization chart.

-----------------------------------------------------

Learning Outcome

After completing this project you will understand:

- How to evaluate classification models
- Differences between accuracy, precision, recall, and F1 score
- When to use each metric
