from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

import os


def read_file():
    file_path = "/opt/airflow/data/input.txt"
    with open(file_path, "r") as file:
        content = file.read()
        print(content)


dag = DAG(
    dag_id='dag_read_file',
    start_date=datetime(2025, 1, 15),
    schedule_interval='@daily',
    catchup=False
)

start_task = DummyOperator(task_id="start")

read_file_task = PythonOperator(
    task_id="read_file_task",
    python_callable=read_file,
    dag=dag
)

bash_read_file = BashOperator(
    task_id='bash_read_file',
    bash_command='cat /opt/airflow/data/input.txt')

stop = DummyOperator(task_id="stop")

start_task >> read_file_task >> bash_read_file >> stop
