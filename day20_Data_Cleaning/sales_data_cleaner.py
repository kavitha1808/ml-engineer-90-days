import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Price": [50000, 20000, None, 50000, None],
    "Quantity": [2, None, 3, 2, 1],
    "City": ["Chennai", "Mumbai", None, "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)

print("Raw Sales Data:\n", df)

df["Price"] = df["Price"].fillna(df["Price"].median())
df["Quantity"] = df["Quantity"].fillna(1)
df["City"] = df["City"].fillna("Unknown")

df = df.drop_duplicates()

df["Revenue"] = df["Price"] * df["Quantity"]

print("\nCleaned Sales Data:\n", df)
print("\nTotal Revenue:", df["Revenue"].sum())
