CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL
);

INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM customers WHERE lastname = 'Smith';

SELECT * FROM customers WHERE lastname = 'Jones';

SELECT * FROM customers WHERE firstname <> 'Scott';
