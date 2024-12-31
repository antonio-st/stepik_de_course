from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2024, 12, 19),
    'owner': 'airflow'
}

dag = DAG(
    'dag_var',
    default_args=default_args,
    description='dag variable',
    schedule_interval='0 8 * * *'  # ежедневное выполнение
)


def my_task():
    my_variable = Variable.get("host1")
    print(my_variable)


bash_ex2 = BashOperator(
    task_id='bash_ex2',
    bash_command='echo "Task 2 now $(date)"',
    dag=dag
)

task = PythonOperator(task_id='my_task', python_callable=my_task)

bash_ex2 >> task
