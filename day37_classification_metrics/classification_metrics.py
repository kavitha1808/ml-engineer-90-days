# Day 37 - Classification Metrics
# Accuracy, Precision, Recall, F1 Score

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Actual labels (True values)
y_true = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

# Predicted labels by model
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

# Precision
precision = precision_score(y_true, y_pred)

# Recall
recall = recall_score(y_true, y_pred)

# F1 Score
f1 = f1_score(y_true, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

print("Confusion Matrix:\n", cm)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
