from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime

with DAG('HttpSensor_dag', schedule_interval='@daily', start_date=datetime(2023, 1, 1)) as dag:

    task1 = DummyOperator(task_id='task1')

    wait_for_api = HttpSensor(
        task_id='wait_for_api',
        http_conn_id='my_http_conn',
        endpoint='https://api.coindesk.com/v1/bpi/currentprice.json'
    )

task1 >> wait_for_api
