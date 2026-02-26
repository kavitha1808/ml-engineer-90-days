-- Get unique cities
SELECT DISTINCT city
FROM orders;

-- Get unique categories
SELECT DISTINCT category
FROM orders;

-- Get distinct city-category combinations
SELECT DISTINCT city, category
FROM orders;

-- Get unique users who spent more than 70000 in a single order
SELECT DISTINCT user_id
FROM orders
WHERE amount > 70000;
