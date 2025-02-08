# select from db
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

        # Создание курсора
        cur = conn.cursor()

        # Выбор данных из таблицы
        cur.execute('SELECT * FROM employees;')
        rows = cur.fetchall()

        # Вывод данных
        for row in rows:
            print(row)

        # Закрытие курсора и соединения
        cur.close()
        conn.close()
        print("PostgreSQL connection closed")

    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")

# Выполнение функции подключения
connect_postgres()