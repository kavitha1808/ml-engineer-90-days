-- Create orders table

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    product VARCHAR(100),
    category VARCHAR(100),
    amount DECIMAL(10,2),
    city VARCHAR(100),
    order_date DATE
);
