import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# Create folders
os.makedirs("outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/titanic.csv")

# ---------------------------
# 1. Raw data preview
# ---------------------------
plt.figure(figsize=(10, 4))
plt.axis("off")
table = plt.table(cellText=df.head().values,
                  colLabels=df.columns,
                  loc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)
plt.title("Raw Data Preview")
plt.savefig("outputs/raw_data_preview.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 2. Missing values heatmap
# ---------------------------
plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.savefig("outputs/missing_values_heatmap.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 3. Target distribution
# ---------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x="Survived", data=df)
plt.title("Target Distribution (Survived)")
plt.savefig("outputs/target_distribution.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 4. Age distribution
# ---------------------------
plt.figure(figsize=(6, 4))
sns.histplot(df["Age"].dropna(), bins=20, kde=True)
plt.title("Age Distribution")
plt.savefig("outputs/age_distribution.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 5. Feature selection
# ---------------------------
features = ["Pclass", "Sex", "Age", "Fare", "Embarked"]
target = "Survived"

X = df[features]
y = df[target]

# ---------------------------
# 6. Preprocessing
# ---------------------------
numeric_features = ["Age", "Fare"]
categorical_features = ["Pclass", "Sex", "Embarked"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# ---------------------------
# 7. Pipeline
# ---------------------------
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(n_estimators=100, random_state=42))
])

# ---------------------------
# 8. Train-test split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------------------
# 9. Train
# ---------------------------
pipeline.fit(X_train, y_train)

# ---------------------------
# 10. Predict
# ---------------------------
y_pred = pipeline.predict(X_test)

# ---------------------------
# 11. Evaluate
# ---------------------------
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}\n")
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.savefig("outputs/confusion_matrix.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 12. Feature Importance
# ---------------------------
ohe = pipeline.named_steps["preprocessor"].named_transformers_["cat"].named_steps["onehot"]
cat_names = ohe.get_feature_names_out(categorical_features)
all_features = numeric_features + list(cat_names)

importances = pipeline.named_steps["model"].feature_importances_

fi = pd.DataFrame({
    "Feature": all_features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=fi.head(10), x="Importance", y="Feature")
plt.title("Top Feature Importances")
plt.savefig("outputs/feature_importance.png", bbox_inches="tight")
plt.close()

# ---------------------------
# 13. Save model
# ---------------------------
joblib.dump(pipeline, "models/random_forest_pipeline.pkl")
print("\nModel saved to models/random_forest_pipeline.pkl")

# ---------------------------
# 14. Sample prediction
# ---------------------------
sample = pd.DataFrame([{
    "Pclass": 3,
    "Sex": "male",
    "Age": 22,
    "Fare": 7.25,
    "Embarked": "S"
}])

prediction = pipeline.predict(sample)[0]
print("\nSample Prediction:", "Survived" if prediction == 1 else "Did Not Survive")
