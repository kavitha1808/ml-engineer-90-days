import pandas as pd

df = pd.read_csv("datasets/sales.csv")

print("===== SALES DATA INSPECTION =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity_Sold"]

print("\nTotal Revenue:")
print(df["Revenue"].sum())

print("\nRevenue by Category:")
print(df.groupby("Category")["Revenue"].sum())
