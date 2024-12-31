from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG('file_sensor', schedule_interval='@daily', start_date=datetime(2024, 12, 24)) as dag:

    start_task = DummyOperator(task_id="start")
    bash_ex1 = BashOperator(
        task_id='bash_ex1',
        bash_command='echo $(ls)')
    stop_task = DummyOperator(task_id="stop")
    t6 = FileSensor(task_id='wait_for_file', filepath='/home/antonio/file.txt')

start_task >> bash_ex1 >> t6 >> stop_task
