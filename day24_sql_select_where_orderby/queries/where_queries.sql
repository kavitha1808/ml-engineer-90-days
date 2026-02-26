-- Orders above 50000
SELECT *
FROM orders
WHERE amount > 50000;

-- Orders from Chennai
SELECT *
FROM orders
WHERE city = 'Chennai';

-- Orders between 1000 and 10000 in Mumbai
SELECT *
FROM orders
WHERE city = 'Mumbai'
AND amount BETWEEN 1000 AND 10000;

-- Orders from specific users
SELECT *
FROM orders
WHERE user_id IN (101, 102);
