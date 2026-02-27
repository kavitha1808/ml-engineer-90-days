# 📊 Day 25 – SQL GROUP BY & Aggregate Functions  
## E-Commerce Sales Analytics Project

---

## 📌 Project Overview

This project demonstrates SQL data analysis using **GROUP BY** and **aggregate functions** on a sample e-commerce dataset.

The objective is to generate meaningful business insights such as:

- Total revenue
- Category-wise revenue
- Customer spending analysis
- Product performance
- Monthly sales trends

This project focuses on mastering SQL aggregation concepts in a clean and structured way.

---

## 🛠 Concepts Covered

- SELECT
- GROUP BY
- Aggregate Functions:
  - SUM()
  - COUNT()
  - AVG()
  - MAX()
  - MIN()
- HAVING clause
- ORDER BY
- Revenue calculation using expressions (price * quantity)

---

## 📂 Project Structure

Day25_SQL_GroupBy_Aggregations/
│
├── dataset/
│   └── orders.csv
│
├── schema/
│   └── create_orders_table.sql
│
├── queries/
│   ├── 01_total_revenue.sql
│   ├── 02_revenue_by_category.sql
│   ├── 03_top_customers.sql
│   ├── 04_product_performance.sql
│   ├── 05_high_value_customers.sql
│   ├── 06_average_order_value.sql
│   └── 07_monthly_revenue.sql
│
└── README.md

---

## 📊 Dataset Description

Table: `orders`

Columns:

- `order_id` – Unique order identifier  
- `user_id` – Customer ID  
- `product` – Product name  
- `category` – Product category  
- `price` – Price per unit  
- `quantity` – Number of units purchased  
- `order_date` – Date of order  

---

## 📈 Business Insights Generated

1. Total company revenue  
2. Revenue by product category  
3. Top spending customers  
4. Most sold products  
5. High-value customers using HAVING clause  
6. Average order value  
7. Monthly revenue analysis  

---

## 🚀 Skills Demonstrated

- SQL aggregation and grouping  
- Business-oriented data analysis  
- Revenue computation  
- Customer segmentation  
- Query structuring for reporting  

---
