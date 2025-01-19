from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG('dag_file_sensor', schedule_interval='@daily', start_date=datetime(2025, 1, 12)) as dag:
    start_task = DummyOperator(task_id="start")
    bash_ex1 = BashOperator(
        task_id='bash_ex1',
        bash_command='echo "test from dag" >> /opt/airflow/logs/test_bash.txt')
    bash_ex2 = BashOperator(
        task_id='bash_ex2',
        bash_command='cat /opt/airflow/logs/test_bash.txt')
    wait_for_file = FileSensor(
        task_id='wait_for_file', filepath="/opt/airflow/logs/test_bash.txt")
    t7 = FileSensor(
        task_id="wait_for_file_async", filepath="/opt/airflow/logs/test_bash.txt", deferrable=True
    )
    stop = DummyOperator(task_id="stop")

start_task >> bash_ex1 >> bash_ex2 >> wait_for_file >> t7>> stop
