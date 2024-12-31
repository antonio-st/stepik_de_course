from airflow import DAG
from airflow.operators.email import EmailOperator

from datetime import datetime

dag = DAG('email_example_dag', start_date=datetime(2024, 12, 20))

task = EmailOperator(
    task_id='send_email',
    to='antonio-st@yandex.ru',
    subject='Airflow Email',
    html_content='<p>This is an Airflow email.</p>',
    dag=dag
)

task
