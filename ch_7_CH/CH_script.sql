-- ClickHouse

CREATE TABLE IF NOT EXISTS default.test(
id UInt32,
column1 String,
column2 String
)
ENGINE = MergeTree()
ORDER BY id;

INSERT INTO `default`.test
	(id, column1, column2)
VALUES
	(1, 'A', 'abc'),
    (2, 'A', 'def'),
    (3, 'B', 'abc'),
    (4, 'B', 'def');
    
   SELECT *
   FROM `default`.test t 
   
   
   -- еще табличка
   CREATE TABLE IF NOT EXISTS `default`.sales_merge_tree
   (
   date DATE,
   product String,
   quantity UInt32,
   price Float32,
   order_id UInt32
   ) 
   ENGINE = MergeTree()
   ORDER BY `date`;
   
   
 INSERT INTO default.sales_merge_tree (date, product, quantity, price, order_id) VALUES
('2023-05-01', 'Widget A', 10, 5.0, 1),
('2023-05-01', 'Widget A', 15, 4.5, 2),
('2023-05-02', 'Gadget B', 20, 10.0, 3);

-- SummingMergeTree

CREATE TABLE IF NOT EXISTS `default`.sales_summing_merge_tree
(
date DATE,
product String,
quantity UInt32,
) ENGINE = SummingMergeTree
ORDER BY `date`;

--Вставим данные о продажах 2х условных товаров/услуг:

INSERT INTO sales_summing_merge_tree (date, product, quantity) VALUES
('2023-05-01', 'Widget A', 10),
('2023-05-02', 'Gadget B', 20),
('2023-05-01', 'Widget A', 11),
('2023-05-02', 'Gadget B', 22),
('2023-05-01', 'Widget A', 12),
('2023-05-02', 'Gadget B', 23);

SELECT *
FROM sales_summing_merge_tree;


--Добавим еще данных, за другие дни:

INSERT INTO sales_summing_merge_tree (date, product, quantity) VALUES
('2023-05-02', 'Widget A', 100),
('2023-05-01', 'Gadget B', 200),
('2023-05-02', 'Widget A', 110),
('2023-05-01', 'Gadget B', 220),
('2023-05-02', 'Widget A', 120),
('2023-05-01', 'Gadget B', 230);

SELECT *
FROM sales_summing_merge_tree;


-- AggregatingMergeTree


CREATE TABLE IF NOT EXISTS `default`.sales_raw -- таблица продаж
(
date_sale Date, 	-- Дата продажи
product_id UInt32,  -- Идентификатор продукта (будет 1 и 2)
quantity UInt32,    -- Количество проданных единиц
price Float32		--Ц ена за единицу товара 
) ENGINE = MergeTree()
ORDER BY date_sale;


-- создаем материализованное представление, которое будет суммировать количество проданных товаров и общую сумму продаж

CREATE MATERIALIZED VIEW IF NOT EXISTS sales_mv
ENGINE = AggregatingMergeTree()
ORDER BY (date_sale, product_id) 
AS
SELECT date_sale
	   ,product_id
	   ,SUM(quantity) AS total_quantity     -- Суммарное количество (агрегация по датам и id продукта)
	   ,SUM(quantity * price) AS total_cost -- Суммарная стоимость проданных товаров (количество * цену)
FROM `default`.sales_raw
GROUP BY date_sale , product_id 


INSERT INTO sales_raw 
VALUES 
    ('2024-06-01', 1, 10, 100.0),
    ('2024-06-01', 1, 7, 100.0),
    ('2024-06-01', 2, 25, 200.0),
    ('2024-06-01', 2, 3, 200.0),
    ('2024-06-01', 2, 8, 200.0),
    ('2024-06-01', 1, 6, 100.0),
    ('2024-06-01', 2, 2, 200.0),
    ('2024-06-01', 2, 12, 200.0),
    ('2024-06-01', 2, 21, 200.0),
    ('2024-06-01', 1, 7, 100.0),
    ('2024-06-01', 2, 20, 200.0),
    ('2024-06-01', 2, 33, 200.0),
    ('2024-06-01', 2, 28, 200.0),
    ('2024-06-01', 1, 7, 100.0);


SELECT *
FROM sales_mv

-- вставим вторую "порцию" данных, уже за следующий день.

INSERT INTO sales_raw 
VALUES 
    ('2024-06-02', 1, 3, 100.0),
    ('2024-06-02', 1, 22, 100.0),
    ('2024-06-02', 2, 5, 200.0),
    ('2024-06-02', 2, 43, 200.0),
    ('2024-06-02', 2, 2, 200.0),
    ('2024-06-02', 1, 4, 100.0),
    ('2024-06-02', 2, 26, 200.0),
    ('2024-06-02', 2, 2, 200.0),
    ('2024-06-02', 2, 1, 200.0),
    ('2024-06-02', 1, 37, 100.0),
    ('2024-06-02', 2, 2, 200.0),
    ('2024-06-02', 2, 12, 200.0),
    ('2024-06-02', 2, 3, 200.0),
    ('2024-06-02', 1, 15, 100.0);

SELECT *
FROM sales_mv


-- ReplacingMergeTree


CREATE TABLE IF NOT EXISTS `default`.replacing_MT
(
key Int64,
event_name String,
event_time DateTime
)
ENGINE = ReplacingMergeTree()
ORDER BY key; 

-- выполним запросы поочередно

INSERT INTO replacing_MT Values (1, 'первая вставка', '2024-03-03 03:03:03');
INSERT INTO replacing_MT Values (1, 'вторая вставка', '2023-01-01 00:00:00');
INSERT INTO replacing_MT Values (1, 'третья вставка', '2022-01-01 00:00:00');

SELECT * 
FROM replacing_MT FINAL


-- аналогично с eventTime
CREATE TABLE default.replacing_MT_with_param
(
    key Int64,
    event_name String,
    eventTime DateTime
)
ENGINE = ReplacingMergeTree (eventTime)
ORDER BY key;

INSERT INTO replacing_MT_with_param Values (1, 'первая вставка', '2024-03-03 03:03:03');
INSERT INTO replacing_MT_with_param Values (1, 'вторая вставка', '2023-01-01 00:00:00');
INSERT INTO replacing_MT_with_param Values (1, 'третья вставка', '2022-01-01 00:00:00');

SELECT *
FROM replacing_MT_with_param FINAL


-- CollapsingMergeTree
-- движок, позволяющий "сворачивать" старые версии строк, помечая их как удалённые, но не удаляя физически.

CREATE TABLE default.sales_collapsing_merge_tree
(
    date Date,
    product String,
    quantity UInt32,
    price Float32,
    order_id UInt32,
    sign Int8
) ENGINE = CollapsingMergeTree(sign)
ORDER BY date;

-- Вставим данные двумя вставками:

INSERT INTO sales_collapsing_merge_tree (date, product, quantity, price, order_id, sign) VALUES
('2023-05-01', 'Widget A', 10, 5.0, 1, 1),
('2023-05-02', 'Gadget B', 20, 10.0, 3, 1);


INSERT INTO sales_collapsing_merge_tree (date, product, quantity, price, order_id, sign) VALUES
('2023-05-01', 'Widget A', 10, 5.0, 1, -1),
('2023-05-01', 'Widget A', 15, 4.5, 2, 1);

SELECT * 
FROM sales_collapsing_merge_tree

SELECT * 
FROM sales_collapsing_merge_tree FINAL


-- VersionedCollapsingMergeTree
-- усовершенствованная версия CollapsingMergeTree, добавляющая поддержку версий строк

CREATE TABLE default.sales_versioned_collapsing_merge_tree
(
    date Date,
    product String,
    quantity UInt32,
    price Float32,
    order_id UInt32,
    sign Int8,
    version Int8
) ENGINE = VersionedCollapsingMergeTree(sign,version)
ORDER BY date;


INSERT INTO sales_versioned_collapsing_merge_tree (date, product, quantity, price, order_id, sign, version) VALUES
('2023-05-01', 'Widget A', 10, 5.0, 1, 1, 1);

INSERT INTO sales_versioned_collapsing_merge_tree (date, product, quantity, price, order_id, sign, version) VALUES
('2023-05-01', 'Widget A', 10, 5.0, 1, -1, 1),
('2023-05-01', 'Widget A', 15, 4.5, 2, 1, 2);

SELECT * 
FROM sales_versioned_collapsing_merge_tree FINAL



