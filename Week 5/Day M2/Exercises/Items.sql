
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;



--Exercise 1 for 19 May
--Part 1
SELECT *
FROM items
ORDER BY price ASC;

--Part 2
SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;

--Part 3
SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC
LIMIT 3;

-- Part 4
SELECT last_name
FROM customers
ORDER BY last_name DESC;

