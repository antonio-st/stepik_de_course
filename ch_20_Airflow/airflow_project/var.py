import requests

# URL для создания переменной
url = 'http://127.0.0.1:8080/api/v1/variables'

# Параметры запроса
headers = {'Content-Type': 'application/json'}
data = {
    'key': 'host2',
    'value': '127.0.0.2'
}

# Отправка POST-запроса для создания переменной
response = requests.post(url, headers=headers, json=data)

# Проверка статуса ответа
if response.status_code == 200:
    print('Переменная успешно создана')
else:
    print('Ошибка при создании переменной:', response.status_code)