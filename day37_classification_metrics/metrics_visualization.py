import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# True and predicted labels
y_true = [1,0,1,1,0,1,0,1,1,0]
y_pred = [1,0,1,0,0,1,0,1,0,0]

accuracy = accuracy_score(y_true,y_pred)
precision = precision_score(y_true,y_pred)
recall = recall_score(y_true,y_pred)
f1 = f1_score(y_true,y_pred)

metrics = ["Accuracy","Precision","Recall","F1 Score"]
values = [accuracy,precision,recall,f1]

plt.bar(metrics,values)
plt.title("Classification Metrics Comparison")
plt.ylabel("Score")
plt.ylim(0,1)
plt.show()
