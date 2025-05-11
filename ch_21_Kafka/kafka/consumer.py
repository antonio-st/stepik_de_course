from kafka import KafkaConsumer
import json
import psycopg2
import signal
import sys

# Создание еще одного потребителя Kafka
consumer = KafkaConsumer(
    'Hello',  # Название топика
    bootstrap_servers='192.168.100.11:9092',  # Адрес ВАШЕГО сервера Kafka
    # Чтение сообщений с самого начала, если это первый запуск
    auto_offset_reset='earliest',
    enable_auto_commit=True,  # Автоматическое обновление смещений (offset)
    group_id='python_reader',  # Группа потребителей
    value_deserializer=lambda x: json.loads(
        x.decode('utf-8'))  # Десериализация сообщений из JSON
)

# Чтение сообщений и вывод их в терминал
try:
    print("В ожидании сообщений...")
    for message in consumer:
        # Вывод сообщения в терминал
        print(f"Получено сообщение из темы 'Hello': {message.value}")
except KeyboardInterrupt:
    print("Consumer остановлен")
finally:
    consumer.close()  # Закрытие потребителя при завершении программы
