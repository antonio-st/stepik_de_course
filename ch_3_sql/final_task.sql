-- ФИНАЛЬНОЕ ЗАДАНИЕ SQL

-- создаем и наполняем таблицы
CREATE TABLE IF NOT EXISTS name (
id_name INT PRIMARY KEY,
name_user VARCHAR
);

INSERT INTO name (id_name, name_user) VALUES
(1, 'Иван'),
(2, 'Петр'),
(3, 'Сидор');

CREATE TABLE IF NOT EXISTS paternal_name(
id_paternal INT PRIMARY KEY,
paternal_name VARCHAR
);

INSERT INTO paternal_name (id_paternal, paternal_name) VALUES
(1, 'Иванович'),
(2, 'Петрович'),
(3, 'Сидорович');

CREATE TABLE IF NOT EXISTS surname (
id_surname INT PRIMARY KEY,
surname_user VARCHAR,
id_name INT,
id_paternal INT,
FOREIGN KEY (id_name) REFERENCES name(id_name),
FOREIGN KEY (id_paternal) REFERENCES paternal_name(id_paternal)
);

INSERT INTO surname (id_surname, surname_user, id_name, id_paternal) VALUES
(1, 'Иванов', 1, 1),
(2, 'Петров', 2, 2),
(3, 'Сидоров', 3, 3);

-- Напишите запрос, результат выполнения которого будет возвращать три Ф.И.О целиком:
-- Иванов Иван Иванович, Петров Петр Петрович, Сидоров Сидор Сидорович, но в обратном алфавитном порядке (по убыванию).

SELECT s.surname_user
	   ,n.name_user
	   ,pn.paternal_name 
FROM surname s
JOIN name n ON n.id_name = s.id_name
JOIN paternal_name pn ON pn.id_paternal = s.id_paternal
ORDER BY s.surname_user DESC;




