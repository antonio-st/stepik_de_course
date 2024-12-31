from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2024, 12, 19),
    'owner': 'airflow',
}

dag = DAG(
    'bash_dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval='0 8 * * *',  # ежедневное выполнение
)

# BashOperator

bash_ex1 = BashOperator(
    task_id='bash_ex1',
    bash_command='echo "Task 1"',
    dag=dag
)

bash_ex2 = BashOperator(
    task_id='bash_ex2',
    bash_command='echo "Task 2 now $(date)"',
    dag=dag
)

bash_ex1 >> bash_ex2  # Определение зависимости между задачами
