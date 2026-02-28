-- Insert Customers
INSERT INTO customers VALUES
(1, 'Ravi'),
(2, 'Anu'),
(3, 'Kiran');

-- Insert Orders
INSERT INTO orders VALUES
(101, 1, '2025-02-01'),
(102, 2, '2025-02-02'),
(103, 1, '2025-02-03');

-- Insert Products
INSERT INTO products VALUES
(201, 'Laptop', 60000),
(202, 'Phone', 20000),
(203, 'Tablet', 30000);

-- Insert Order Items
INSERT INTO order_items VALUES
(101, 201, 1),
(101, 202, 2),
(102, 203, 1),
(103, 202, 1);

-- Insert Payments
INSERT INTO payments VALUES
(1, 101, 100000),
(2, 102, 30000),
(3, 103, 20000);
