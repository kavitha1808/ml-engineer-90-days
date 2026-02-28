# 📘 Day 26 – SQL JOINs (Inner Join, Left Join & Multi-Table Queries)

## 📌 Overview
This project demonstrates relational database concepts using SQL JOIN operations.

It covers:
- INNER JOIN
- LEFT JOIN
- Multi-table JOINs
- Revenue aggregation using GROUP BY

The project simulates a small e-commerce database.

---

## 🗂 Database Structure

Tables used:

1. customers
2. orders
3. products
4. order_items
5. payments

These tables are connected using Primary Key and Foreign Key relationships.

---

## 🔗 Concepts Practiced

### 1️⃣ INNER JOIN
Returns only matching rows from both tables.

Example:
Customers who have placed orders.

### 2️⃣ LEFT JOIN
Returns all rows from the left table and matching rows from the right table.

Example:
All customers including those who have not placed orders.

### 3️⃣ Multi-Table JOIN
Combines 5 tables to generate a full transaction report including:
- Customer Name
- Product Name
- Quantity Purchased
- Payment Amount

This demonstrates relational chaining and multi-table thinking.

### 4️⃣ Aggregation with JOIN
Calculates total revenue per customer using SUM() and GROUP BY.

---

## 🧠 Learning Outcome

After completing this project, I can:

- Understand relational database design
- Connect multiple tables using JOIN
- Write clean multi-table queries
- Perform aggregation after JOIN
- Think in terms of foreign key relationships

---

## ▶️ How to Run

1. Run `schema.sql` to create tables.
2. Run `sample_data.sql` to insert data.
3. Execute queries from `joins_queries.sql`.

---

## 🚀 Skills Demonstrated

- SQL JOIN operations
- Foreign Key relationships
- Multi-table querying
- Data aggregation
- Relational thinking
