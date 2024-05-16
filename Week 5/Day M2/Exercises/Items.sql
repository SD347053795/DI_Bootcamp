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
