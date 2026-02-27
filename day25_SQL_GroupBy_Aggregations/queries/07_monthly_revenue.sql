-- Monthly revenue analysis

SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(price * quantity) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;
