-- Sort by amount ascending
SELECT *
FROM orders
ORDER BY amount ASC;

-- Sort by amount descending
SELECT *
FROM orders
ORDER BY amount DESC;

-- Sort by city then by amount descending
SELECT *
FROM orders
ORDER BY city ASC, amount DESC;
