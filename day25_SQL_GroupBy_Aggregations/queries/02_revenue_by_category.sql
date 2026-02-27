-- Revenue generated per category

SELECT 
    category,
    SUM(price * quantity) AS total_revenue
FROM orders
GROUP BY category
ORDER BY total_revenue DESC;
