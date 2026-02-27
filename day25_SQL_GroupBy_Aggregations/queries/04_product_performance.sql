-- Most sold products by quantity

SELECT 
    product,
    SUM(quantity) AS total_units_sold
FROM orders
GROUP BY product
ORDER BY total_units_sold DESC;
