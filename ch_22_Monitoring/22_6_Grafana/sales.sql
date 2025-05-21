CREATE TABLE sales (
    sale_date Date,
    product_id UInt32,
    category String,
    units_sold UInt32,
    revenue Float64
) ENGINE = MergeTree()
ORDER BY sale_date;

INSERT INTO sales VALUES
('2024-08-20', 1, 'Electronics', 50, 2500.00),
('2024-08-20', 2, 'Clothing', 30, 1500.00),
('2024-08-20', 3, 'Books', 20, 400.00),
('2024-08-21', 1, 'Electronics', 60, 3000.00),
('2024-08-21', 2, 'Clothing', 25, 1250.00),
('2024-08-21', 3, 'Books', 15, 300.00),
('2024-08-22', 1, 'Electronics', 70, 3500.00),
('2024-08-22', 2, 'Clothing', 20, 1000.00),
('2024-08-22', 3, 'Books', 25, 500.00);

SELECT *
FROM sales