import pandas as pd


def run_sales_analysis():
    df = pd.read_csv("data/sales_data.csv")

    region_sales = df.groupby("Region")["Sales"].sum()
    category_avg = df.groupby("Category")["Sales"].mean()
    region_category = df.groupby(["Region", "Category"])["Sales"].sum()

    result = region_sales.reset_index(name="Total_Sales")
    result.to_csv("outputs/sales_results.csv", index=False)

    print("\nSales Analysis Completed")
    print(result)
