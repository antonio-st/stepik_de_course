import psycopg2

# Подключение к PostgreSQL
def connect_postgres():
    try:
        # Эта функция открывает соединение с PostgreSQL. Она принимает несколько параметров:
        conn = psycopg2.connect(
            host="localhost",
            port="5436",
            database="mydb",
            user="postgres",
            password="postgres"
        )
        print("Connected to PostgreSQL")
        # Курсор — это объект, который позволяет выполнять SQL-запросы в базе данных через подключение.
        # С его помощью мы можем отправлять запросы к базе данных и получать результаты.
        cur = conn.cursor()
        cur.execute('SELECT version()')
        # Эта строка извлекает одну строку результата запроса
        db_version = cur.fetchone()
        print("PostgreSQL version:", db_version)
        # Закрывает курсор после выполнения запроса.
        cur.close()
        # Закрывает подключение к базе данных. Это важный шаг, чтобы освободить ресурсы.
        conn.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
connect_postgres()