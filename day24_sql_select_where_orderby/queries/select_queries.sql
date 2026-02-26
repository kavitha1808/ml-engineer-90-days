-- Retrieve all columns
SELECT * FROM orders;

-- Retrieve specific columns
SELECT order_id, user_id, amount FROM orders;

-- Rename columns using alias
SELECT order_id AS id,
       amount AS order_value
FROM orders;
