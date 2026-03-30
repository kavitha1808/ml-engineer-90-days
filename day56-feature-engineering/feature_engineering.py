import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:\n", df.head())

# -----------------------------
# 1. Handling Missing Values
# -----------------------------
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# -----------------------------
# 2. Encoding Categorical Data
# -----------------------------
df = pd.get_dummies(df, columns=['City'], drop_first=True)

# -----------------------------
# 3. Feature Scaling
# -----------------------------
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# -----------------------------
# 4. Feature Creation
# -----------------------------
df['Age_Salary_Ratio'] = df['Age'] / (df['Salary'] + 1)

# -----------------------------
# 5. Binning (Discretization)
# -----------------------------
df['Age_Group'] = pd.cut(df['Age'], bins=3, labels=['Young', 'Middle', 'Old'])

# -----------------------------
# 6. Feature Selection
# -----------------------------
from sklearn.feature_selection import SelectKBest, f_classif

X = df.drop('Purchased', axis=1)
y = df['Purchased']

# Convert categorical labels to numeric
X = pd.get_dummies(X, drop_first=True)

selector = SelectKBest(score_func=f_classif, k=3)
X_new = selector.fit_transform(X, y)

print("\nSelected Features Shape:", X_new.shape)

# -----------------------------
# Final Data
# -----------------------------
print("\nProcessed Data:\n", df.head())
