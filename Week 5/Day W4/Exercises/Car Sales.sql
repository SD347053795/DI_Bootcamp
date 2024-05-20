SELECT * FROM public."Orders"
CREATE TABLE orders (
    customer_id INT,
    order_date DATE,
    product_name VARCHAR(50),
    quantity INT,
    price DECIMAL(10, 2),
    region VARCHAR(50)
);

INSERT INTO orders (customer_id, order_date, product_name, quantity, price, region) VALUES
(101, '2024-01-10', 'Laptop', 2, 1200.00, 'North America'),
(102, '2024-01-11', 'Smartphone', 5, 800.00, 'Europe'),
(103, '2024-01-12', 'Office Chair', 1, 150.00, 'Asia'),
(101, '2024-01-13', 'Coffee Maker', 10, 90.00, 'North America'),
(104, '2024-01-14', 'Headphones', 3, 200.00, 'Europe'),
(105, '2024-02-15', 'Laptop', 1, 1200.00, 'Europe'),
(102, '2024-02-16', 'Smartphone', 2, 800.00, 'North America'),
(103, '2024-02-17', 'Office Chair', 5, 150.00, 'Europe'),
(106, '2024-02-18', 'Coffee Maker', 7, 90.00, 'Asia'),
(107, '2024-02-19', 'Headphones', 4, 200.00, 'North America'),
(108, '2024-03-10', 'Laptop', 3, 1200.00, 'Asia'),
(109, '2024-03-11', 'Smartphone', 6, 800.00, 'Europe'),
(110, '2024-03-12', 'Office Chair', 2, 150.00, 'North America'),
(111, '2024-03-13', 'Coffee Maker', 8, 90.00, 'Europe'),
(112, '2024-03-14', 'Headphones', 5, 200.00, 'Asia');

SELECT product_name,region, SUM(quantity) AS total_quantity, SUM(quantity * price) AS total_sales
FROM orders
GROUP BY product_name, region
HAVING 
    SUM(quantity * price) > 2000;


SELECT product_name, DATE_FORMAT(order_date, '%Y-%m') AS order_month, AVG(price) AS average_price
FROM orders
GROUP BY product_name, DATE_FORMAT(order_date, '%Y-%m')
HAVING 
    AVG(price) > 500;


SELECT customer_id, region, COUNT(order_id) AS total_orders, SUM(quantity) AS total_quantity
FROM orders
GROUP BY customer_id, region
HAVING 
    COUNT(customer_id) >= 2;

