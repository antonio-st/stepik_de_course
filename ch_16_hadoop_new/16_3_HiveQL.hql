-- удалить таблицу
DROP TABLE employees;

-- смотрим БД
SHOW DATABASES;
SHOW SCHEMAS;

-- Перед тем, как просматриваются таблицы, всегда выбирается база данных (если она одна - выбирать не приходится).
USE database_name;

--смотрим таблицы
SHOW TABLES;
SHOW TABLES in default
-- Если таблиц много, то можно использовать префикс
SHOW TABLES LIKE 'prefix_%';

-- чтобы узнать, какая база данных используется по умолчанию, можно ввести следующую команду
SELECT current_database();

-- создаем БД
CREATE DATABASE employees;
CREATE DATABASE IF NOT EXISTS employees;
-- с описанием
CREATE DATABASE employees COMMENT 'Employee database for HR management system';

-- создание db с указанием пути
CREATE DATABASE employees LOCATION '/user/hive/databases/employees';

-- описание БД
DESCRIBE DATABASE employees;



CREATE TABLE employees (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

INSERT INTO TABLE employees
VALUES
    (1, 'John Doe', 'HR', 50000.0),
    (2, 'Jane Smith', 'Finance', 60000.0),
    (3, 'Alice Johnson', 'Engineering', 55000.0);

INSERT INTO TABLE employees
SELECT id, name, department, salary
FROM employees
WHERE salary > 50000.0;

SELECT * FROM employees WHERE department = 'Engineering';

SELECT * FROM employees ORDER BY salary DESC;

SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;

SELECT id, name, COUNT(*)
FROM employees
GROUP BY id, name
HAVING COUNT(*) > 1;

SELECT MAX(salary) AS max_salary FROM employees;

-- не сработает из-за настроек конфига
UPDATE employees
SET salary = salary * 1.1;