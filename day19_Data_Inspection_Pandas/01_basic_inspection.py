import pandas as pd

# Load dataset
df = pd.read_csv("datasets/employee_data.csv")

print("🔹 First 5 Rows")
print(df.head())

print("\n🔹 Dataset Information")
df.info()

print("\n🔹 Statistical Summary")
print(df.describe())

print("\n🔹 Data Types")
print(df.dtypes)

print("\n🔹 Missing Values")
print(df.isnull().sum())
