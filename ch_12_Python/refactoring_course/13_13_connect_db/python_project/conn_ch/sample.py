import clickhouse_connect

# Подключение к ClickHouse
def connect_clickhouse():
    try:
        # Установка соединения с ClickHouse
        client = clickhouse_connect.get_client(host='localhost', port=8123)
        print("Connected to ClickHouse")

        # Создание таблицы
        client.command('''
        CREATE TABLE IF NOT EXISTS employees (
            id UInt32,
            name String,
            position String,
            salary Float32
        ) ENGINE = MergeTree()
        ORDER BY id;
        ''')
        print("Table 'employees' created in ClickHouse")

        # Вставка данных в таблицу
        client.command('''
        INSERT INTO employees (id, name, position, salary) VALUES
        (1, 'Alice', 'Manager', 70000),
        (2, 'Bob', 'Developer', 60000),
        (3, 'Charlie', 'Designer', 50000);
        ''')
        print("Data inserted into 'employees' table in ClickHouse")

        # Выбор данных из таблицы
        result = client.query('SELECT * FROM employees;')
        rows = result.result_rows

        # Вывод данных
        for row in rows:
            print(row)

        print("ClickHouse connection closed")

    except Exception as e:
        print(f"Error connecting to ClickHouse: {e}")


# Выполнение функции подключения
connect_clickhouse()