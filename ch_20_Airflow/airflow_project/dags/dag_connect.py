from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.hooks.base_hook import BaseHook

default_args = {
    'start_date': datetime(2024, 12, 19),
    'owner': 'airflow'
}

dag = DAG(
    'dag_connect',
    default_args=default_args,
    description='dag_connect',
    schedule_interval='0 8 * * *'  # ежедневное выполнение
)

bash_ex1 = BashOperator(
    task_id='bash_ex1',
    bash_command='echo "Task 1"',
    dag=dag
)


def my_task():
    my_conn = BaseHook.get_connection("my_postgres")
    print(f"Host: {my_conn.host}")
    print(f"Login: {my_conn.login}")


task_get_conn = PythonOperator(
    task_id='task_get_conn', python_callable=my_task)

bash_ex1 >> task_get_conn
