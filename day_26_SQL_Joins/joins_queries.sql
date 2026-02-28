-- =========================================
-- INNER JOIN: Customers with their Orders
-- =========================================

SELECT c.name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;



-- =========================================
-- LEFT JOIN: All Customers with Orders
-- =========================================

SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;



-- =========================================
-- Multi-Table JOIN: Full Transaction Report
-- =========================================

SELECT 
    c.name,
    p.product_name,
    oi.quantity,
    pay.amount
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
INNER JOIN payments pay
    ON o.order_id = pay.order_id;



-- =========================================
-- Total Revenue Per Customer
-- =========================================

SELECT 
    c.name,
    SUM(pay.amount) AS total_revenue
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN payments pay
    ON o.order_id = pay.order_id
GROUP BY c.name;
