--SELECT * FROM customer;
--SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
--SELECT create_date FROM customer GROUP BY create_date;
--SELECT * FROM customer ORDER BY first_name DESC;
--SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
--SELECT address, phone FROM address WHERE district = 'Texas';
--SELECT * FROM film WHERE film_id = 15 OR film_id = 150;
--SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Agent Truman';
--SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'ag%';
--SELECT film_id, title, description, length, rental_rate, replacement_cost FROM film ORDER BY replacement_cost ASC limit 10;
--SELECT film_id, title, description, length, rental_rate, replacement_cost FROM film ORDER BY replacement_cost ASC limit 10 OFFSET 10;

--SELECT c.first_name, c.last_name, p.amount, p.payment_date
--FROM payment as p
--LEFT JOIN customer as c
--ON p.customer_id = c.customer_id
--ORDER BY c.customer_id DESC;

--SELECT title FROM film WHERE film_id not in (SELECT film_id FROM inventory);

--SELECT country.country, city.city
--FROM city
--INNER JOIN country
--ON city.country_id = country.country_id
--ORDER BY country.country;

--SELECT customer_id, first_name, last_name, amount, payment_date, staff_id
--FROM customer
--INNER JOIN payment
--USING(customer_id)
--ORDER BY staff_id;
