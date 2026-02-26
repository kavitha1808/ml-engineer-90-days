# 📊 SQL Fundamentals – SELECT, WHERE, ORDER BY, DISTINCT

## 📌 Overview

This project demonstrates foundational SQL operations using a real-world e-commerce dataset.

It focuses on:

- Data retrieval using `SELECT`
- Filtering data using `WHERE`
- Sorting results using `ORDER BY`
- Removing duplicate results using `DISTINCT`

> Note: No aggregation functions are used in this project.

---

## 🗂 Dataset Description

**Table:** `orders`

| Column      | Description               |
|-------------|--------------------------|
| order_id    | Unique order identifier  |
| user_id     | Customer ID              |
| product     | Product name             |
| category    | Product category         |
| amount      | Order value              |
| city        | Customer city            |
| order_date  | Date of order            |

---

## 🚀 Concepts Covered

### 1️⃣ SELECT
- Retrieve all columns
- Retrieve specific columns
- Column aliasing using `AS`

### 2️⃣ WHERE
- Filtering using comparison operators (`=`, `>`, `<`, `>=`, `<=`)
- `AND` / `OR` conditions
- `BETWEEN` operator
- `IN` operator

### 3️⃣ ORDER BY
- Ascending sorting (`ASC`)
- Descending sorting (`DESC`)
- Multi-column sorting

### 4️⃣ DISTINCT
- Removing duplicate values
- Distinct on single column
- Distinct on multiple columns

---

## 💡 Learning Outcome

After completing this project, you will be able to:

- Write clean and structured SQL queries
- Filter large datasets efficiently
- Sort data using different strategies
- Extract unique values from datasets
- Understand SQL query execution flow at a foundational level

---

## 🛠 How to Run

1. Run `schema.sql` to create the table.
2. Run `data.sql` to insert sample data.
3. Execute queries from the `queries/` folder.

---

## 💻 Compatible With

- MySQL  
- PostgreSQL  
- SQLite  

---

## 📈 Project Level

Beginner → Foundation Level SQL 
(Preparation for aggregation and advanced querying in next phase)


