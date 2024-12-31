### Запуск образа

 Создайте  главную папку для вашего проекта Airflow. Например, airflow_project
Внутри этой папки создайте три подпапки: dags, logs, и plugins

   Необходимо скачать файл docker-compose.yaml
   https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml

    и поместить его в папку airflow_project.

```
docker-compose up airflow-init
docker-compose up -d
```

### Параметры Default Args

Параметры default_args используются для определения значений по умолчанию для атрибутов в объекте DAG (Directed Acyclic Graph) в Apache Airflow. Эти параметры могут быть применены ко всем задачам (операторам) внутри этого DAG, если для них не указаны собственные значения. Вот некоторые распространенные параметры default_args:

1.      owner (str): Владелец или автор DAG. Это имя пользователя или группы, ответственных за данный DAG.

2.      depends_on_past (bool): Определяет, зависит ли выполнение каждой задачи от успешного завершения ее предыдущей итерации (если True).

3.      start_date (datetime): Дата и время, с которой начинается выполнение DAG. Это может быть указано как строка в формате 'YYYY-MM-DD' или объект datetime.

4.      end_date (datetime): Дата и время, после которых выполнение DAG больше не будет запускаться. Обычно используется для установки конечного срока выполнения DAG.

5.      retries (int): Количество попыток выполнения задачи в случае ошибки.

6.      retry_delay (timedelta): Время задержки между попытками выполнения задачи в случае ошибки.

7.      email (str): Адрес электронной почты, на который будут отправляться уведомления о статусе выполнения DAG.

8.      email_on_failure (bool): Указывает, следует ли отправлять уведомления о неудачных попытках выполнения задачи по электронной почте.

9.      email_on_retry (bool): Указывает, следует ли отправлять уведомления о повторных попытках выполнения задачи по электронной почте.
10.     10.  schedule_interval (str or timedelta): Интервал, с которым запускается DAG. Может быть строкой в формате «cron» или объектом timedelta.
11.     max_active_runs (int): Максимальное количество активных запусков DAG одновременно.
12.     catchup (bool): Определяет, должен ли DAG выполнять задачи для пропущенных интервалов времени, если это включено.


### Переменные (Variables): 

Переменные в Airflow представляют собой ключ-значение пары, которые могут быть использованы для хранения конфигурационных данных и параметров, доступных в вашем рабочем процессе. 

Некоторые примеры использования переменных могут включать настройки подключения к базе данных, настройки авторизации и другие параметры, которые могут меняться в зависимости от окружения выполнения. Переменные можно определить и настроить через веб-интерфейс Airflow или использовать API для программного управления ими. 

Для доступа к переменным в коде задачи вы можете использовать объект Variable модуля airflow.models.



### Подключения (Connections): 

Подключения в Airflow представляют собой параметры, необходимые для установки связи с внешними источниками данных, такими как базы данных, сервисы облачных провайдеров, API и другие ресурсы. Эти параметры, такие как хост, порт, имя пользователя, пароль и другие, могут быть настроены и управляются в веб-интерфейсе Airflow или через API. 

Подключения в Airflow могут быть использованы в коде задач для установки соединения с внешними источниками данных. 

Для доступа к подключениям в коде задачи вы можете использовать объект Connection модуля airflow.hooks.base.

### XCom: 

XCom (Cross Communication) в Airflow представляет собой механизм обмена данными между задачами внутри рабочего процесса. XCom позволяет передавать и получать данные между задачами в виде ключ-значение пары. Это может быть полезно, когда вам нужно передать результат выполнения одной задачи в другую задачу для дальнейшей обработки. 

Задачи могут читать и записывать XCom значения с использованием методов xcom_pull() и xcom_push() соответственно. Для доступа к XCom значениям в коде задачи вы можете использовать объект context (контекст выполнения) и методы модуля airflow.models.




### Создание подключений через веб-интерфейс Airflow:

    Перейдите в веб-интерфейс Airflow ( доступен по адресу http://localhost:8080).
    В меню выберите «Admin» и затем «Connections».
    Нажмите кнопку «Create» или «Add Connection».
    Заполните поля для подключения, такие как Conn Id (идентификатор подключения), Conn Type (тип подключения), Host, Port, Login, Password и другие, в зависимости от типа подключения.
    Нажмите кнопку «Save» или «Add».


### XComs (Cross-Communication)

XComs, или механизм кросс-коммуникации, позволяет задачам в Airflow обмениваться сообщениями или данными между собой. Каждая задача может "вытолкнуть" сообщение в XCom с помощью метода xcom_push, и другие задачи могут "вытянуть" это сообщение с помощью метода xcom_pull.

Это особенно полезно в сценариях, где результат выполнения одной задачи требуется для начала выполнения другой. Например, задача, которая обрабатывает данные, может передать результаты другой задаче, которая использует эти данные для обновления базы данных или отправки уведомлений.

XComs хранятся в базе данных Airflow, что делает этот механизм надежным и эффективным для управления данными между задачами.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def push_data(**context):
    context['ti'].xcom_push(key='my_data', value='Hello, Airflow!')

def process_data(**context):
    my_data = context['ti'].xcom_pull(key='my_data')
    print(my_data)

with DAG('xcom_example_dag', schedule_interval='@daily', start_date=datetime(2024, 1, 1)) as dag:
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push_data,
        provide_context=True
    )

    process_task = PythonOperator(
        task_id='process_task',
        python_callable=process_data,
        provide_context=True
    )

    push_task >> process_task

    ```


В этом примере у нас есть две задачи: push_task и process_task.

В задаче push_task мы определяем функцию push_data(), которая отправляет данные 'Hello, Airflow!' в XCom с помощью метода xcom_push(). Мы используем аргумент **context, чтобы получить доступ к контексту выполнения задачи, и вызываем context['ti'].xcom_push() для отправки данных в XCom. Мы указываем ключ 'my_data' и значение 'Hello, Airflow!'.

В задаче process_task мы определяем функцию process_data(), которая получает данные из XCom с помощью метода xcom_pull(). Мы снова используем аргумент **context, чтобы получить доступ к контексту выполнения задачи, и вызываем context['ti'].xcom_pull() с ключом 'my_data', чтобы получить данные из XCom. Затем мы просто выводим полученные данные.

Затем мы связываем задачи push_task и process_task с помощью оператора >>, чтобы определить порядок их выполнения.

При выполнении этого DAG задача push_task сначала отправляет данные в XCom, а затем задача process_task получает эти данные из XCom и выводит их.


### Погружение в операторы Airflow. Sensor операторы

В Apache Airflow сенсоры (Sensors) используются для мониторинга определенных условий или событий и ожидания, пока эти условия не будут выполнены. Сенсоры позволяют вам создавать задачи, которые ожидают внешние события или изменения состояний, прежде чем продолжить выполнение DAG. Вот некоторые примеры сенсорных операторов в Airflow:

1. ExternalTaskSensor: Этот сенсор ожидает завершения определенной задачи (внешней задачи) в другом DAG. Вот пример использования ExternalTaskSensor:

```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sensors import ExternalTaskSensor
from datetime import datetime

with DAG('my_dag', schedule_interval='@daily', start_date=datetime(2023, 1, 1)) as dag:
    task1 = DummyOperator(task_id='task1')

    task2 = ExternalTaskSensor(task_id='wait_for_task1', external_dag_id='other_dag', external_task_id='task1')

    task1 >> task2
```

2. FileSensor: Этот сенсор ожидает появление определенного файла на файловой системе. Вот пример использования FileSensor:

```python
from airflow import DAG
from airflow.operators.sensors import FileSensor

from datetime import datetime

with DAG('my_dag', schedule_interval='@daily', start_date=datetime(2023, 1, 1)) as dag:
  wait_for_file = FileSensor(
      task_id='wait_for_file',
      filepath='/path/to/my/file.txt'
  )
```

В этом примере у нас есть задача wait_for_file, которая ожидает появление файла /path/to/my/file.txt на файловой системе. Когда файл будет обнаружен, задача wait_for_file продолжит выполнение.

3. HttpSensor: Этот сенсор выполняет HTTP-запрос и ожидает успешный ответ от сервера. Вот пример использования HttpSensor:

```python
from airflow import DAG
from airflow.operators.sensors import HttpSensor

from datetime import datetime

with DAG('my_dag', schedule_interval='@daily', start_date=datetime(2023, 1, 1)) as dag:
    wait_for_api = HttpSensor(
        task_id='wait_for_api',
        http_conn_id='my_http_conn',
        endpoint='/api/health'
    )
```
В этом примере у нас есть задача wait_for_api, которая выполняет HTTP-запрос на эндпоинт /api/health с использованием соединения с идентификатором 'my_http_conn'. Сенсор ожидает успешный ответ от сервера (код ответа 2xx). Когда успешный ответ будет получен, задача wait_for_api продолжит выполнение.
