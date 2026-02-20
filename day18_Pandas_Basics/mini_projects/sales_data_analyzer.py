import pandas as pd


def analyze_sales():
    df = pd.read_csv("sales.csv")

    df["Revenue"] = df["Price"] * df["Quantity"]

    print("Sales Data with Revenue:\n", df)

    print("\nTotal Revenue:", df["Revenue"].sum())

    best_selling = df.loc[df["Quantity"].idxmax()]
    print("\nBest Selling Product:\n", best_selling)

    category_revenue = df.groupby("Category")["Revenue"].sum()
    print("\nRevenue by Category:\n", category_revenue)


if __name__ == "__main__":
    analyze_sales()
