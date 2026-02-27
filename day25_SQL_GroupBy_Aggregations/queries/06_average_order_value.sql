-- Average order value

SELECT 
    AVG(price * quantity) AS average_order_value
FROM orders;
