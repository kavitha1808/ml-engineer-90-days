-- Calculate total revenue

SELECT 
    SUM(price * quantity) AS total_revenue
FROM orders;
