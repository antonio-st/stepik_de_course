-- Создаем таблицу "customers"
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR,
    email VARCHAR
);

-- Создаем таблицу "products"
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR,
    price_per_unit DECIMAL(5, 2)
);

-- Создаем таблицу "orders"
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Вставляем данные в таблицу "customers" с новыми значениями customer_id
INSERT INTO customers (customer_id, name, email) VALUES
    (101, 'Иван Иванов', 'ivanov@mymail.tu'),
    (102, 'Петр Петров', 'petrov@mymail.tu'),
    (103, 'Максим Максимов', 'maximov@mymail.tu'),
    (104, 'Алексей Алексеев', 'alexeev@mymail.tu');

-- Вставляем данные в таблицу "products"
INSERT INTO products (product_id,product_name, price_per_unit) VALUES
    (1,'Флешка', 10.00),
    (2,'Клавиатура', 15.00),
    (3,'Наушники', 20.00);

-- Вставляем данные в таблицу "orders"
INSERT INTO orders (order_id, order_date, customer_id, product_id, quantity) 
VALUES
    (1, '2024-05-01', 101, 1, 1),
    (2, '2024-05-01', 102, 2, 1),
    (3, '2024-05-01', 103, 3, 1),
    (4, '2024-05-01', 104, 1, 3),
    (5, '2024-05-01', 101, 2, 1),
    (6, '2024-05-02', 101, 1, 3),
    (7, '2024-05-02', 102, 2, 2),
    (8, '2024-05-02', 103, 3, 1),
    (9, '2024-05-02', 104, 1, 1),
    (10, '2024-05-02', 101, 2, 2),
    (11, '2024-05-03', 101, 1, 1),
    (12, '2024-05-03', 102, 2, 2),
    (13, '2024-05-03', 103, 3, 1),
    (14, '2024-05-03', 104, 1, 4),
    (15, '2024-05-03', 101, 2, 1),
    (16, '2024-05-04', 101, 1, 1),
    (17, '2024-05-04', 102, 2, 1),
    (18, '2024-05-04', 103, 3, 1),
    (19, '2024-05-04', 104, 1, 1),
    (20, '2024-05-04', 101, 2, 1);
    
   
   -- Получить общее количество заказанных единиц каждого товара
   
   SELECT order_date 
   		  ,product_id 
   		  ,SUM(quantity) AS total_quantity
   FROM stepik_de_shop.orders o 
   GROUP BY order_date, product_id
   ORDER BY order_date, product_id
   
      -- Получить общее количество заказанных единиц каждого товара, чтобы в результате его выполнения были только строки со значениями 
      --total_quantity > 2:
   
      SELECT order_date 
   		  ,product_id 
   		  ,SUM(quantity) AS total_quantity
   FROM stepik_de_shop.orders o 
   GROUP BY order_date, product_id
   HAVING SUM(quantity) > 2
   ORDER BY order_date, product_id
   
   
--   Напишите запрос для выбора всех заказов, где количество товаров больше среднего количества товаров всех заказов. 
--   В результатах должны быть order_id, customer_id, product_id и quantity.
   
   SELECT order_id, 
        customer_id, 
        product_id,
        quantity
FROM stepik_de_shop.orders
WHERE quantity > (SELECT AVG(quantity)
                FROM stepik_de_shop.orders)
                
-- статистика  инфосайта
CREATE TABLE site_visit_log (
    timestamp TIMESTAMP,
    uniq_id INT
)             

-- статистика  интернет-магазина
CREATE TABLE shop_visit_log (
    timestamp TIMESTAMP,
    uniq_id INT
)

-- Заполняем таблицу "site_visit_log" данными
INSERT INTO site_visit_log (timestamp, uniq_id) VALUES
    ('2024-05-01 09:15:22', 123456),
    ('2024-05-01 10:30:45', 234567),
    ('2024-05-01 11:45:18', 345678),
    ('2024-05-01 12:10:55', 456789),
    ('2024-05-01 13:25:37', 567890),
    ('2024-05-01 14:40:12', 678901),
    ('2024-05-01 15:05:28', 789012),
    ('2024-05-01 16:20:17', 890123),
    ('2024-05-01 17:35:44', 901234),
    ('2024-05-01 18:50:29', 123045),
    ('2024-05-01 09:15:22', 123456),
    ('2024-05-01 10:30:45', 234567),
    ('2024-05-01 11:45:18', 345678),
    ('2024-05-01 12:10:55', 456789),
    ('2024-05-01 13:25:37', 567890),
    ('2024-05-01 14:40:12', 678901),
    ('2024-05-01 15:05:28', 789012),
    ('2024-05-01 16:20:17', 890123),
    ('2024-05-01 17:35:44', 901234),
    ('2024-05-01 18:50:29', 123045);
   
   -- Заполняем таблицу "shop_visit_log" данными
INSERT INTO shop_visit_log (timestamp, uniq_id) VALUES
    ('2024-05-01 09:25:12', 234567),
    ('2024-05-01 10:20:22', 345678),
    ('2024-05-01 11:35:15', 456789),
    ('2024-05-01 12:40:56', 567890),
    ('2024-05-01 13:55:33', 678901),
    ('2024-05-01 14:24:15', 789012),
    ('2024-05-01 15:15:22', 890123),
    ('2024-05-01 16:42:15', 901234),
    ('2024-05-01 17:25:21', 123045),
    ('2024-05-01 18:40:13', 234156),
    ('2024-05-01 09:17:56', 234567),
    ('2024-05-01 12:52:13', 345678),
    ('2024-05-01 11:15:16', 456789),
    ('2024-05-01 12:54:15', 567890),
    ('2024-05-01 13:25:22', 678901),
    ('2024-05-01 14:42:15', 789012),
    ('2024-05-01 15:25:23', 890123),
    ('2024-05-01 16:00:16', 901234),
    ('2024-05-01 17:35:47', 123045),
    ('2024-05-01 18:30:21', 234156);
   
   
   
   
   
   /*
    * 
Напишите запрос, чтобы определить общую стоимость заказов для каждого клиента за весь период, 
отсортированную по стоимости в убывающем порядке.
Результат должен содержать:
name, total_cost
    * 
*/
   
   
   SELECT c.name
       ,SUM(price_per_unit) AS total_cost
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products ppu ON ppu.product_id = o.product_id
GROUP BY name
ORDER BY total_cost DESC;

-- Напишите верный запрос чтобы найти товары, которые были заказаны только одним клиентом.
SELECT p.product_name
FROM orders o
JOIN products p ON o.product_id = p.product_id 
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY p.product_name
HAVING COUNT(DISTINCT c.name) = 1;


-- оконные функции

SELECT order_id, order_date, quantity,
		SUM(quantity) OVER (PARTITION BY(order_date)),
		AVG(quantity) OVER (PARTITION BY(order_date)),
		MIN(quantity) OVER (PARTITION BY(order_date)),
		MAX(quantity) OVER (PARTITION BY(order_date)),
		COUNT(quantity) OVER (PARTITION BY (order_date))
FROM stepik_de_shop.orders o 


-- Функции ранжирования
-- ROW_NUMBER(): Назначает уникальный номер каждой строке в пределах окна.

SELECT order_id, order_date, quantity,
		ROW_NUMBER () OVER (PARTITION BY order_date ORDER BY quantity DESC)
FROM stepik_de_shop.orders o 


-- LAG(): Возвращает значение из предыдущей строки в пределах окна. Параметры функции указываются в скобках (столбец и шаг смещения).

SELECT order_id, order_date, quantity,
	LAG(quantity) OVER(ORDER BY order_date)
FROM stepik_de_shop.orders o 


-- LEAD(): Возвращает значение из следующей строки в пределах окна.

SELECT order_id, order_date, quantity,
	LEAD(quantity) OVER(ORDER BY order_date)
FROM stepik_de_shop.orders o 

SELECT order_id, order_date, quantity,
FIRST_VALUE(quantity) OVER(PARTITION BY order_date) AS first_quantity
FROM stepik_de_shop.orders 


SELECT order_id, order_date, quantity,
LAST_VALUE(quantity) OVER(PARTITION BY order_date) AS first_quantity
FROM stepik_de_shop.orders 

UPDATE stepik_de_shop.orders
SET quantity = 3 
WHERE order_id = 6


-- Функции, работающие с рамками (frames)

-- ROWS BETWEEN Устанавливает рамку на основе числа строк относительно текущей строки.

SELECT order_id, order_date, quantity,
       SUM(quantity) OVER (ORDER BY order_date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS sum_around
FROM orders;

-- RANGE BETWEEN: Устанавливает рамку на основе значений в строках относительно текущей строки.
SELECT order_id, order_date, quantity,
       SUM(quantity) OVER (ORDER BY order_date RANGE BETWEEN INTERVAL '1 DAY' PRECEDING AND CURRENT ROW) AS range_sum
FROM orders;

TRUNCATE TABLE stepik_de_shop.orders

/*
 * SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]
    [ * | expression [ [ AS ] output_name ] [, ...] ]
    [ FROM from_item [, ...] ]
    [ WHERE condition ]
    [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
    [ HAVING condition ]
    [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
    [ ORDER BY expression [ ASC | DESC | USING operator ] [ NULLS { FIRST | LAST } ] [, ...] ]
    [ LIMIT { count | ALL } ]
    [ OFFSET start [ ROW | ROWS ] ]
    [ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
    [ FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE } [ OF table_name [, ...] ] [ NOWAIT | SKIP LOCKED ] [...] ]

 * 
 * */



