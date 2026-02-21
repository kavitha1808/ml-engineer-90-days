import pandas as pd

df = pd.read_csv("datasets/employee_data.csv")

print("===== EMPLOYEE DATA INSPECTION =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Convert data types
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Department"] = df["Department"].astype("category")

print("\nUpdated Data Types:")
print(df.dtypes)
