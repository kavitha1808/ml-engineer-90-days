-- Total spending per customer

SELECT 
    user_id,
    SUM(price * quantity) AS total_spent
FROM orders
GROUP BY user_id
ORDER BY total_spent DESC;
