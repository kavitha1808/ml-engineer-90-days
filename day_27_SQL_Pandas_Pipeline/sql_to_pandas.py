import sqlite3
import pandas as pd


def fetch_all_orders():
    conn = sqlite3.connect("ecommerce.db")

    query = "SELECT * FROM orders"
    df = pd.read_sql_query(query, conn)

    conn.close()
    return df


def fetch_high_value_orders(min_amount=10000):
    conn = sqlite3.connect("ecommerce.db")

    query = f"""
    SELECT *
    FROM orders
    WHERE amount > {min_amount}
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


def main():
    # Load all orders
    df = fetch_all_orders()
    print("All Orders:")
    print(df)

    # Load high value orders
    high_value_df = fetch_high_value_orders()

    # Save output
    high_value_df.to_csv("outputs/high_value_orders.csv", index=False)

    print("\nHigh value orders saved to outputs/high_value_orders.csv")


if __name__ == "__main__":
    main()
