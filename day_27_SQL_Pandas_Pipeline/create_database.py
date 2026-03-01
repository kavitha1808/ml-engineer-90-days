import sqlite3


def create_database():
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    # Create orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL
    )
    """)

    # Insert sample data
    sample_data = [
        ("Kavitha", "Laptop", 55000),
        ("Rahul", "Phone", 20000),
        ("Anita", "Headphones", 3000),
        ("Kavitha", "Mouse", 800),
        ("Rahul", "Monitor", 15000)
    ]

    cursor.executemany("""
    INSERT INTO orders (customer_name, product, amount)
    VALUES (?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()

    print("Database created and sample data inserted successfully.")


if __name__ == "__main__":
    create_database()
