--CREATE TABLE items (
--item_id SERIAL PRIMARY KEY,
--item VARCHAR NOT NULL,
--price INT NOT NULL
--);

--CREATE TABLE customers (
--customer_id SERIAL PRIMARY KEY,
--customer_name VARCHAR (50) NOT NULL,
--customer_surname VARCHAR (100) NOT NULL
--);

--INSERT INTO items (item, price)
--VALUES ('Small Desk', 100),
--('Large desk', 300),
--('Fan', 80);

--INSERT INTO customers (customer_name, customer_surname)
--VALUES ('Greg', 'Jones'),
--('Sandra', 'Jones'),
--('Scott', 'Scott'),
--('Trevor', 'Green'),
--('Melanie', 'Johnson');

--SELECT * FROM items;
--SELECT * FROM customers;
--SELECT * FROM items WHERE price > 80;
--SELECT * FROM items WHERE price <= 300;
--SELECT * FROM customers WHERE customer_surname = 'Smith';
--Nothing
--SELECT * FROM customers WHERE customer_surname = 'Jones';
--SELECT * FROM customers WHERE customer_name <> 'Scott';