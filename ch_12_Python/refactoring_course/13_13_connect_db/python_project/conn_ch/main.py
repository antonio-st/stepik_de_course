import clickhouse_connect

# Подключение к ClickHouse
def connect_clickhouse():
    try:
        client = clickhouse_connect.get_client(host='localhost', port=8123)
        print("Connected to ClickHouse")
        version = client.command('SELECT version()')
        print("ClickHouse version:", version)
    except Exception as e:
        print(f"Error connecting to ClickHouse: {e}")

connect_clickhouse()