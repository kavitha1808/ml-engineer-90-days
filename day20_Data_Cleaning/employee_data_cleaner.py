import pandas as pd
import numpy as np

data = {
    "Name": ["Kavitha", "Arun", "Divya", "Arun", None],
    "Age": [25, None, 29, None, 30],
    "Salary": [50000, 60000, None, 60000, 52000],
    "Department": ["IT ", "HR", None, "HR", "Finance"],
    "Experience": [2, 5, None, 5, 3]
}

df = pd.DataFrame(data)

print("Raw Data:\n", df)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Experience"] = df["Experience"].fillna(0)
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# Remove rows where Name missing
df = df.dropna(subset=["Name"])

# Clean text
df["Department"] = df["Department"].str.strip()

# Fix data types
df["Age"] = df["Age"].astype(int)
df["Experience"] = df["Experience"].astype(int)

print("\nCleaned Data:\n", df)
