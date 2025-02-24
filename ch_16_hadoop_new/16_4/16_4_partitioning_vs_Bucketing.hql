-- PARTITIONED BY — указывает колонки, по которым будет производиться партицирование.
-- FIELDS TERMINATED BY — указывает разделитель колонок (в данном случае, запятая).

CREATE TABLE employees_partitioned (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
PARTITIONED BY (year INT, month INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Далее создадим 2 файла на локальной машине. 

-- Первый - data_2024_11.csv
-- Второй - data_2024_12.csv

docker cp data_2024_11.csv 39f82136cacf:/tmp/data_2024_12.csv
docker cp data_2024_12.csv 39f82136cacf:/tmp/data_2024_12.csv


hdfs dfs -put /tmp/data_2024_11.csv /user/hive/warehouse/employees_partitioned/year=2024/month=11/
hdfs dfs -put /tmp/data_2024_12.csv /user/hive/warehouse/employees_partitioned/year=2024/month=12/

-- Теперь начинается самое интересное.

--  Нам необходимо сказать Hive о том, что у нас есть партиции. Сделать это можно следующей командой.

ALTER TABLE employees_partitioned ADD PARTITION (year=2024, month=11)
LOCATION '/user/hive/warehouse/employees_partitioned/year=2024/month=11';

ALTER TABLE employees_partitioned ADD PARTITION (year=2024, month=12)
LOCATION '/user/hive/warehouse/employees_partitioned/year=2024/month=12';

------------------- бакетирование  -------------------

-- Бакетирование — это разбиение данных на фиксированное количество сегментов (бакетов) на основе хэш-функции, примененной к одному или нескольким столбцам.

--     Hive делит данные на бакеты с использованием хэш-функции по указанному столбцу и делением на количество бакетов.
--     Например, если данные бакетированы по id на 4 бакета, то строки будут распределены по бакетам так:

-- hash(id) % 4

-- Создадим следующую таблицу - 

    -- CLUSTERED BY указывает колонку для хэширования.
    -- INTO 4 BUCKETS означает, что таблица будет разделена на 4 бакета.
    -- STORED AS TEXTFILE указывает формат хранения данных.


CREATE TABLE employees_bucketed (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
CLUSTERED BY (id) INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Для загрузки данных в бакетированную таблицу нужно включить соответствующие настройки:
SET hive.enforce.bucketing = true;

-- А теперь перейдем в Hive и попробуем с локальной системы подгрузить данные сразу же в Hive, основываясь на HDFS

-- Так как поплясать с бубном пришлось, то вот что я делал:

SET hive.enforce.bucketing = true; 
SET hive.exec.dynamic.partition = true; 
SET hive.exec.dynamic.partition.mode = nonstrict; 
SET hive.strict.checks.bucketing = false;  
SET hive.mapred.mode = nonstrict; 

CREATE TABLE employees_bucketed_tmp (
id INT,
name STRING,
department STRING,
salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE employees_bucketed (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
CLUSTERED BY (id) INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE; 

LOAD DATA LOCAL INPATH '/tmp/data.csv' INTO TABLE employees_bucketed_tmp; 

INSERT OVERWRITE TABLE employees_bucketed 
SELECT * FROM employees_bucketed_tmp; 

-- hdfs dfs -ls /user/hive/warehouse/employees_bucketed/


------------------ использование обоих методов вместе. ------------------


--временная таблица
CREATE TABLE temp_table (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT, 
    year INT, 
    month INT
    ) 
    ROW FORMAT DELIMITED 
    FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE;
-- использование обоих методов вместе
CREATE TABLE employees_partitioned_bucketed (
id INT,
name STRING,
department STRING,
salary FLOAT
)
PARTITIONED BY (year INT, month INT)
CLUSTERED BY (id) INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

--загрузка во временную таблицу
LOAD DATA LOCAL INPATH '/tmp/part_bac_test.csv' INTO TABLE temp_table;

--загрузка из временной таблицы
INSERT OVERWRITE TABLE employees_partitioned_bucketed PARTITION (year, month)
SELECT id, name, department, salary, year, month FROM temp_table;