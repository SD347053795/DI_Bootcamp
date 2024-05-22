--1
UPDATE film
SET language_id = 6
WHERE title IN ('Motions Details', 'Moulin Wake', 'Mourning Purple', 'Movie Shakespeare', 'Mulan Moon', 'Mulholland Beast');

--2 
SELECT 
    tc.constraint_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu 
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu 
      ON ccu.constraint_name = tc.constraint_name
WHERE tc.table_name = 'customer' AND tc.constraint_type = 'FOREIGN KEY';

--3 
DROP TABLE customer_review;
--This can be easy if there aren't any dependencies, however if there are dependiencies then you will need to add CASTCADE I believe

--4
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

--5
SELECT f.title, f.rental_rate
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

--6.1
SELECT title
FROM film
WHERE description LIKE '%sumo wrestler%'
AND (actor_1_first_name = 'Penelope' OR actor_1_last_name = 'Penelope' OR actor_2_first_name = 'Penelope' OR actor_2_last_name = 'Penelope');

--6.2
SELECT title
FROM film
WHERE length < '01:00:00'
AND rating = 'R';

--6.3
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND r.rental_rate > 4.00
AND r.rental_date BETWEEN '2005-07-28' AND '2005-08-01';

--6.4
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title LIKE '%boat%' OR f.description LIKE '%boat%')
AND f.replacement_cost > 20.00; 
