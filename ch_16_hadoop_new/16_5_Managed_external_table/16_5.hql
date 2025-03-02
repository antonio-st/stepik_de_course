-- Внутренние таблицы (Managed Tables)

--     Hive полностью управляет данными, хранящимися в таблице.
--     Данные сохраняются в папке Hive (обычно в warehouse директории).
--     При удалении таблицы данные также удаляются.
--     Данные находятся в HDFS в директории, определяемой переменной hive.metastore.warehouse.dir (по умолчанию /user/hive/warehouse).

-- По умолчанию создается внутренняя таблица, если явно не указать, что таблица внешняя.

-- Внешние таблицы (External Tables)

--     Hive использует данные, которые находятся за пределами управления Hive (например, в определенной папке HDFS).
--     Удаление таблицы не удаляет данные — только метаданные.
--     Hive не удаляет данные, если таблица удаляется — удаляются только записи о таблице в метасторе.

-- А далее рассмотрим примеры создания и работы с обоими типами таблиц.

-- Для создания внутренней таблицы будем использовать следующий код -

CREATE TABLE internal_table (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Видим, что таблица создана. И по умолчанию - она внутренняя. Откроем терминал и откроем рядышком HDFS.

hdfs dfs -ls /user/hive/warehouse/

-- Попробуем залить в эту таблицу данные в Hive.

INSERT INTO TABLE internal_table VALUES
(1, 'John Doe', 'HR', 50000.0),
(2, 'Jane Smith', 'Finance', 60000.0),
(3, 'Alice Johnson', 'Engineering', 55000.0);


-- Теперь попробуем дропнуть внутреннюю таблицу и посмотрим, а удалятся ли файлы из HDFS.

DROP TABLE internal_table;

--root@9591729654cd:/opt# hdfs dfs -ls -h /user/hive/warehouse/internal_table
-- ls: `/user/hive/warehouse/internal_table': No such file or directory
-- папка с данными удалена

-- Для создания внешней таблицы нам понадобиться следующий скрипт - 

CREATE EXTERNAL TABLE external_table (
    id INT,
    name STRING,
    department STRING,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/external_data/employees/';


-- в Hive нельзя напрямую использовать команду INSERT для заполнения внешней таблицы. Внешние таблицы в Hive предполагают, что данные уже существуют в указанной директории в HDFS, а Hive просто ссылается на эти данные.

-- Тогда нам необходимо положить данные в эту директорию и потом уже Hive их увидит. Создадим локально файл с расширением csv - 

-- 1,John Doe,HR,50000.0
-- 2,Jane Smith,Finance,60000.0
-- 3,Alice Johnson,Engineering,55000.0

-- Далее закинем файл в докер.

-- docker cp data_ext.csv 9591729654cd:/tmp/data_ext.csv
-- Далее в терминале, где открыт HDFS выполните команду перемещения файла из докера (как бы локальное место) в HDFS.

-- hive> SELECT * FROM external_table;
-- OK
-- 1       John Doe        HR      50000.0
-- 2       Jane Smith      Finance 60000.0
-- 3       Alice Johnson   Engineering     55000.0

DROP TABLE external_table;

hive> SELECT * FROM external_table;
FAILED: SemanticException [Error 10001]: Line 1:14 Table not found 'external_table'



