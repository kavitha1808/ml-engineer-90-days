import pandas as pd
import numpy as np

data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Age": [45, None, 60, 50, None],
    "Blood_Pressure": [120, 130, None, 140, 135],
    "Diabetes": ["Yes", None, "No", "Yes", "No"],
    "Cholesterol": [200, 180, 220, None, 210]
}

df = pd.DataFrame(data)

print("Raw Hospital Data:\n", df)

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Blood_Pressure"] = df["Blood_Pressure"].fillna(df["Blood_Pressure"].mean())
df["Cholesterol"] = df["Cholesterol"].fillna(df["Cholesterol"].mean())
df["Diabetes"] = df["Diabetes"].fillna("No")

df["Diabetes"] = df["Diabetes"].map({"Yes": 1, "No": 0})

print("\nCleaned Hospital Data:\n", df)
