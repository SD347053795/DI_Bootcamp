--P1.1
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

--P1.2
INSERT INTO Customer (first_name, last_name) VALUES ('John', 'Doe');
INSERT INTO Customer (first_name, last_name) VALUES ('Jerome', 'Lalu');
INSERT INTO Customer (first_name, last_name) VALUES ('Lea', 'Rive');

--P1.3
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (true, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe'));
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (false, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

--P1.4
SELECT Customer.first_name
FROM Customer
JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id
WHERE CustomerProfile.isLoggedIn = true;

SELECT Customer.first_name, COALESCE(CustomerProfile.isLoggedIn, false) AS isLoggedIn
FROM Customer
LEFT JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id;

SELECT COUNT(Customer.id) AS NotLoggedInCustomers
FROM Customer
LEFT JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id
WHERE CustomerProfile.isLoggedIn IS NULL OR CustomerProfile.isLoggedIn = false;

--P2.1
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

--P2.2
INSERT INTO Book (title, author) VALUES ('Alice In Wonderland', 'Lewis Carroll');
INSERT INTO Book (title, author) VALUES ('Harry Potter', 'J.K Rowling');
INSERT INTO Book (title, author) VALUES ('To Kill a Mockingbird', 'Harper Lee');

--P2.3
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

--P2.4
INSERT INTO Student (name, age) VALUES ('John', 12);
INSERT INTO Student (name, age) VALUES ('Lera', 11);
INSERT INTO Student (name, age) VALUES ('Patrick', 10);
INSERT INTO Student (name, age) VALUES ('Bob', 14);

--P2.5
CREATE TABLE Library (
    book_fk_id INT,
    student_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_id),
    FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

--P2.6
INSERT INTO Library (book_fk_id, student_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
);

INSERT INTO Library (book_fk_id, student_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
);

INSERT INTO Library (book_fk_id, student_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
);

INSERT INTO Library (book_fk_id, student_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

--P2.7 (Display the Data)
--P2.7.1
SELECT * FROM Library;
--P2.7.2
SELECT Student.name, Book.title
FROM Library
JOIN Student ON Library.student_id = Student.student_id
JOIN Book ON Library.book_fk_id = Book.book_id;
--P2.7.3
SELECT AVG(Student.age) AS average_age
FROM Library
JOIN Student ON Library.student_id = Student.student_id
JOIN Book ON Library.book_fk_id = Book.book_id
WHERE Book.title = 'Alice In Wonderland';
--P2.7.4
DELETE FROM Student WHERE name = 'John';
