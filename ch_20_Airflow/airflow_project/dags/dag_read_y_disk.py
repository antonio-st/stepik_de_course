from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import requests
from urllib.parse import urlencode


def read_file():
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    public_key = 'https://disk.yandex.ru/d/a3gqElPRi8J2Ug'  # Ваша публичная ссылка

    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)

    if response.status_code == 200:
        try:
            # Используем .get() для безопасного доступа к 'href'
            download_url = response.json().get('href')
            if download_url:
                # Загружаем файл
                download_response = requests.get(download_url)

                # Отображаем содержимое файла
                file_content = download_response.content.decode(
                    'utf-8')  # Декодируем байты в строку
                print(file_content)  # Выводим содержимое файла в консоль
            else:
                print("Ключ 'href' отсутствует в ответе.")
        except ValueError:
            print(f"Невозможно декодировать JSON из ответа: {response.text}")
    else:
        print(f'Ошибка: {response.status_code}, {response.text}')


dag = DAG(
    dag_id='dag_read_y_disk',
    start_date=datetime(2023, 10, 1),
    schedule_interval='@daily',
    catchup=False
)

dag.docs_md = """\
#### Даг с помощью api загружает содержимое файла с yandex disk
"""

read_file_task = PythonOperator(
    task_id='read_file_task',
    python_callable=read_file,
    dag=dag
)
