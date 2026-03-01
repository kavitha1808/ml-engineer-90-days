# Day 27 – SQL to Pandas Data Pipeline

## 📌 Overview

This project demonstrates how to connect a SQLite database with Python and load SQL query results into a Pandas DataFrame.

It simulates a simple e-commerce dataset and performs basic data extraction and analysis.

---

## 🛠 Technologies Used

- Python
- SQLite (sqlite3)
- Pandas

---

## 📂 Project Structure
day_27_SQL_Pandas_Pipeline/
│
├── create_database.py        # Creates database and inserts sample data
├── sql_to_pandas.py          # Loads SQL data into Pandas
├── outputs/
│   └── high_value_orders.csv # Filtered results
└── README.md

---

## 🚀 How to Run

1. Install dependencies:

pip install pandas

2. Create database:

python create_database.py

3. Run SQL to Pandas pipeline:

python sql_to_pandas.py

---

## 📊 Features Implemented

- SQLite database creation
- Table creation with PRIMARY KEY auto increment
- Insert multiple records using executemany()
- Load SQL data into Pandas using read_sql_query()
- Filter high-value orders (amount > 10000)
- Export results to CSV

---

## 🧠 Concepts Covered

- Database connection handling
- SQL query execution in Python
- PRIMARY KEY auto increment behavior
- SQL filtering using WHERE clause
- Data export using Pandas

---

## 🎯 Learning Outcome

By completing this project, you understand how:

Database → SQL Query → Python → Pandas → CSV

This is the foundation of real-world data pipelines used in analytics and machine learning workflows.
