# insert and select from db
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

        # Создание таблицы
        cur.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                position VARCHAR(100),
                salary NUMERIC
            );
            ''')
        print("Table 'employees' created")

        # Вставка данных в таблицу
        cur.execute('''
            INSERT INTO employees (name, position, salary)
            VALUES ('Alice', 'Manager', 70000),
                   ('Bob', 'Developer', 60000),
                   ('Charlie', 'Designer', 50000);
            ''')
        print("Data inserted into 'employees' table")

        # Сохранение изменений
        conn.commit()

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