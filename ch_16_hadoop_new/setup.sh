git clone https://github.com/big-data-europe/docker-hive.git

docker-compose up -d

docker exec -it docker-hive-hive-metastore-1 /bin/bash

hive

# проверка
CREATE TABLE employees (id INT, name STRING, salary FLOAT);

INSERT INTO employees VALUES
(1, 'Alice', 5000.00),
(2, 'Bob', 6000.50),
(3, 'Charlie', 7000.75);

SELECT * FROM employees;

