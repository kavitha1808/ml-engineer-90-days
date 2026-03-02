import pandas as pd

# Load dataset
df = pd.read_csv("data/sample_data.csv")

print("===== Dataset Preview =====")
print(df.head())

print("\n===== Data Types =====")
print(df.dtypes)

print("\n===== Statistical Summary =====")
print(df.describe())

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Correlation Matrix =====")
print(df.corr(numeric_only=True))
