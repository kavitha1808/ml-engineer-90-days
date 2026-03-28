import os
import pickle
import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Create folders
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# Predictions before saving
y_pred_before = model.predict(X_test_scaled)
acc_before = accuracy_score(y_test, y_pred_before)

print("Accuracy before saving:", round(acc_before, 4))

# Save model and scaler using Pickle
with open("models/model_pickle.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/scaler_pickle.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save model and scaler using Joblib
joblib.dump(model, "models/model_joblib.pkl")
joblib.dump(scaler, "models/scaler_joblib.pkl")

print("Models saved successfully using Pickle and Joblib!")

# Load model and scaler using Pickle
with open("models/model_pickle.pkl", "rb") as f:
    loaded_model_pickle = pickle.load(f)

with open("models/scaler_pickle.pkl", "rb") as f:
    loaded_scaler_pickle = pickle.load(f)

# Predict using loaded Pickle model
X_test_pickle = loaded_scaler_pickle.transform(X_test)
y_pred_pickle = loaded_model_pickle.predict(X_test_pickle)
acc_pickle = accuracy_score(y_test, y_pred_pickle)

print("Accuracy after loading with Pickle:", round(acc_pickle, 4))

# Load model and scaler using Joblib
loaded_model_joblib = joblib.load("models/model_joblib.pkl")
loaded_scaler_joblib = joblib.load("models/scaler_joblib.pkl")

# Predict using loaded Joblib model
X_test_joblib = loaded_scaler_joblib.transform(X_test)
y_pred_joblib = loaded_model_joblib.predict(X_test_joblib)
acc_joblib = accuracy_score(y_test, y_pred_joblib)

print("Accuracy after loading with Joblib:", round(acc_joblib, 4))

# Save classification report
report = classification_report(y_test, y_pred_joblib, target_names=iris.target_names)

with open("outputs/classification_report.txt", "w", encoding="utf-8") as f:
    f.write("Classification Report (Loaded Joblib Model)\n")
    f.write("=" * 50 + "\n\n")
    f.write(report)

print("Classification report saved to outputs/classification_report.txt")
