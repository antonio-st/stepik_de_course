CREATE TABLE positions (
id INT PRIMARY KEY,
title VARCHAR,
salary INT
);

CREATE TABLE persons (
id INT PRIMARY KEY,
name VARCHAR,
position_id INT,
FOREIGN KEY (position_id) REFERENCES positions(id)
)

INSERT INTO positions(id, title, salary) VALUES
	(1, 'Программист', '1500'),
	('2', 'Юрист', '700'),
	('3', 'HR', '700'),
	('4', 'Дизайнер', '700'),
	('5', 'Маркетолог', '500'),
	('6', 'Data Engineer', '3000');
	
SELECT *
FROM positions p 

INSERT INTO stepik_de.persons (id, name, position_id) VALUES
	('1', 'Владимир', '4'),
	('2', 'Алёна', '1'),
	('3', 'Евгений', '5'),
	('4', 'Артём', '2'),
	('5', 'Борис', '4'),
	('6', 'Татьяна', '3');

SELECT *
FROM stepik_de.persons p 

-- Напишите запрос для добавления в таблицу должности "Повар", с id =7 и зарплатой 777 у.е.

INSERT INTO stepik_de.positions (id, title, salary) VALUES
('7', 'Повар', '777')

-- Напишите запрос, который позволит узнать название должностей у которых зарплата меньше либо равна 500 у.е.

SELECT title
FROM positions
WHERE salary <= 500

-- Напишите запрос, который позволит узнать название должностей у которых id равен 3

SELECT title
FROM positions
WHERE id = 3

-- Напишите запрос, который позволит узнать зарплату у должности "Программист"

SELECT salary 
FROM stepik_de.positions p
WHERE title = 'Программист'


SELECT COUNT(DISTINCT *)
FROM stepik_de.positions

-- FULL JOIN 
SELECT *
FROM positions FULL JOIN persons
ON positions.id = persons.position_id



