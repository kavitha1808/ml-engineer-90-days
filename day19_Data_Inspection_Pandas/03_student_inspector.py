import pandas as pd

df = pd.read_csv("datasets/students.csv")

print("===== STUDENT DATA INSPECTION =====")

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Marks:")
print(df.max(numeric_only=True))

print("\nLowest Marks:")
print(df.min(numeric_only=True))

print("\nAverage Marks:")
print(df.mean(numeric_only=True))
