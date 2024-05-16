SELECT * FROM public."Actors"

CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '1970-08-10', 5),
       ('George', 'Clooney', '1961-06-05', 2),
       ('Angelina', 'Jolie', '1975-06-04', 1),
       ('Jennifer', 'Aniston', '1969-02-11', 0);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Leonardo', 'DiCaprio', '1974-11-11', 1),
       ('Meryl', 'Streep', '1949-06-22', 3),
       ('Tom', 'Hanks', '1956-07-09', 2);

SELECT * FROM actors;

SELECT * FROM actors WHERE first_name = 'Matt';

SELECT * FROM actors WHERE number_oscars >= 3;

SELECT last_name FROM actors WHERE first_name != 'Matt';

SELECT first_name, last_name FROM actors WHERE first_name = 'Matt' AND last_name = 'Damon';

SELECT first_name, last_name FROM actors WHERE first_name = 'Matt' AND last_name = 'Clooney';

SELECT first_name FROM actors WHERE first_name = 'Matt' OR number_oscars = 2;

SELECT first_name FROM actors WHERE last_name LIKE '%y';

SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY first_name ASC;

SELECT * FROM actors LIMIT 4;

SELECT * FROM actors ORDER BY last_name DESC LIMIT 4;

SELECT * FROM actors WHERE first_name LIKE '%e%';

SELECT * FROM actors WHERE number_oscars >= 5;