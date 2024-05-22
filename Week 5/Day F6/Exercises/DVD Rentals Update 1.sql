--1
SELECT * FROM language;

--2
SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

--3
SELECT f.title, f.description, l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;

--4
CREATE TABLE new_film (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

--4
CREATE TABLE IF NOT EXISTS new_film (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
INSERT INTO new_film (name) VALUES ('Air Bud'), ('Free Willy'), ('The Lion King'), ('Toy Story');


--5
CREATE TABLE customer_review (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    film_id INT,
    language_id INT,
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id)
);

--6
INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
VALUES 
(1, 1, 'Great Film!', 9, 'This film was fantastic, with a gripping plot and great performances.'),
(2, 2, 'Not Bad', 7, 'It was a decent film but had some slow parts.');

--7
DELETE FROM new_film WHERE id = 1;

SELECT * FROM new_film; SELECT * FROM customer_review;
DELETE FROM new_film WHERE id = 1;
SELECT * FROM new_film; SELECT * FROM customer_review;

--Any review associated with the deleted film (film_id = 1) will also be removed from the customer_review table
