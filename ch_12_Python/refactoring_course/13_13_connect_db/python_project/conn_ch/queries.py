# select from db
import clickhouse_connect

# Подключение к ClickHouse
def connect_clickhouse():
    try:
        # Установка соединения с ClickHouse
        client = clickhouse_connect.get_client(host='localhost', port=8123)
        print("Connected to ClickHouse")

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