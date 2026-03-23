import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay


# =========================================================
# 1. CREATE OUTPUT FOLDER
# =========================================================
os.makedirs("outputs", exist_ok=True)


# =========================================================
# 2. CREATE A SMALL SYNTHETIC DATASET
#    (Numerical + Categorical + Missing Values)
# =========================================================
data = {
    "age": [25, 32, 47, 51, 62, 23, 40, np.nan, 36, 29, 55, 48, 33, 41, np.nan],
    "salary": [30000, 50000, 70000, 65000, 90000, 28000, 60000, 52000, np.nan, 45000, 85000, 72000, 48000, 61000, 58000],
    "city": ["Chennai", "Bangalore", "Mumbai", "Chennai", "Delhi", "Mumbai", "Delhi", "Chennai", np.nan, "Bangalore", "Delhi", "Mumbai", "Chennai", "Bangalore", "Delhi"],
    "gender": ["F", "M", "M", "F", "M", "F", np.nan, "M", "F", "F", "M", "M", "F", "M", "F"],
    "bought": [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

print("\n=== Raw Dataset ===")
print(df)


# =========================================================
# 3. SAVE RAW DATA PREVIEW AS IMAGE
# =========================================================
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.head(10).values,
                 colLabels=df.columns,
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)
plt.title("Raw Data Preview (First 10 Rows)")
plt.savefig("outputs/raw_data_preview.png", bbox_inches='tight')
plt.close()


# =========================================================
# 4. TARGET DISTRIBUTION PLOT
# =========================================================
plt.figure(figsize=(6, 4))
df["bought"].value_counts().sort_index().plot(kind="bar")
plt.title("Target Distribution (Bought)")
plt.xlabel("Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/target_distribution.png")
plt.close()


# =========================================================
# 5. MISSING VALUES HEATMAP (SIMPLE VISUAL)
# =========================================================
plt.figure(figsize=(8, 4))
plt.imshow(df.isnull(), aspect='auto', cmap='gray_r')
plt.title("Missing Values Heatmap")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.xticks(ticks=range(len(df.columns)), labels=df.columns, rotation=45)
plt.tight_layout()
plt.savefig("outputs/missing_values_heatmap.png")
plt.close()


# =========================================================
# 6. SPLIT FEATURES AND TARGET
# =========================================================
X = df.drop("bought", axis=1)
y = df["bought"]

# Define column types
num_features = ["age", "salary"]
cat_features = ["city", "gender"]


# =========================================================
# 7. PREPROCESSING PIPELINES
# =========================================================

# Numerical pipeline:
# - Fill missing values with mean
# - Scale values
num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Categorical pipeline:
# - Fill missing values with most frequent
# - One-hot encode categories
cat_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both pipelines
preprocessor = ColumnTransformer(transformers=[
    ("num", num_transformer, num_features),
    ("cat", cat_transformer, cat_features)
])


# =========================================================
# 8. FULL ML PIPELINE (PREPROCESSING + MODEL TOGETHER)
# =========================================================
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LogisticRegression())
])


# =========================================================
# 9. TRAIN-TEST SPLIT
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# =========================================================
# 10. TRAIN THE PIPELINE
# =========================================================
pipeline.fit(X_train, y_train)


# =========================================================
# 11. MAKE PREDICTIONS
# =========================================================
y_pred = pipeline.predict(X_test)


# =========================================================
# 12. EVALUATION
# =========================================================
accuracy = accuracy_score(y_test, y_pred)

print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# =========================================================
# 13. PREDICTION DISTRIBUTION PLOT
# =========================================================
plt.figure(figsize=(6, 4))
pd.Series(y_pred).value_counts().sort_index().plot(kind="bar")
plt.title("Prediction Distribution")
plt.xlabel("Predicted Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/prediction_distribution.png")
plt.close()


# =========================================================
# 14. CONFUSION MATRIX PLOT
# =========================================================
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("outputs/confusion_matrix.png")
plt.close()


# =========================================================
# 15. SHOW PIPELINE STEPS
# =========================================================
print("\n=== Pipeline Steps ===")
for name, step in pipeline.named_steps.items():
    print(f"{name}: {step}")


# =========================================================
# 16. EXAMPLE: PREDICT ON NEW DATA
# =========================================================
new_data = pd.DataFrame({
    "age": [38],
    "salary": [62000],
    "city": ["Chennai"],
    "gender": ["F"]
})

new_prediction = pipeline.predict(new_data)

print("\n=== New Data Prediction ===")
print(new_data)
print("Predicted Bought Class:", new_prediction[0])


# =========================================================
# 17. END MESSAGE
# =========================================================
print("\nAll output images saved inside the 'outputs/' folder.")
