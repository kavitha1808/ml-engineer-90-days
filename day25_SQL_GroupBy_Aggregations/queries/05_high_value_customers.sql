-- Customers spending more than 50000

SELECT 
    user_id,
    SUM(price * quantity) AS total_spent
FROM orders
GROUP BY user_id
HAVING SUM(price * quantity) > 50000;
