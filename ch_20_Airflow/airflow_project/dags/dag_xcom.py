from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime


def push_data(**context):
    context['ti'].xcom_push(key='my_data', value='Hello, Airflow!')


def process_data(**context):
    my_data = context['ti'].xcom_pull(key='my_data')
    print(my_data)


default_args = {
    'start_date': datetime(2024, 12, 19),
    'owner': 'airflow'
}

dag = DAG(
    'xcom_example_dag',
    default_args=default_args,
    description='xcom example dag',
    schedule_interval='0 8 * * *'  # ежедневное выполнение
)

start = EmptyOperator(task_id='start', dag=dag)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_data,
    provide_context=True,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_task',
    python_callable=process_data,
    provide_context=True,
    dag=dag
)

end = EmptyOperator(task_id='end', dag=dag)

start >> push_task >> process_task >> end
