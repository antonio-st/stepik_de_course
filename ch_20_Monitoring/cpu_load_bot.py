import psutil
import requests
import time


# Функция для отправки сообщения в Telegram
def send_telegram_alert(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response


# Параметры Telegram
bot_token = "7840843505:AAFMj2fq5sL2qv1PPZBsAog6BM51cAPt8vI"
chat_id = "213407163"

# Пороговое значение для загрузки CPU (в процентах)
cpu_threshold = 51

while True:
    # Получаем загрузку CPU и RAM
    cpu_usage = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    print(f"CPU: {cpu_usage}, RAM: {mem}")
    # Проверяем, превышает ли загрузка CPU пороговое значение
    if cpu_usage > cpu_threshold:
        message = f"Внимание! Высокая загрузка CPU: {cpu_usage}%\nRAM: {mem}"
        response = send_telegram_alert(bot_token, chat_id, message)
    else:
        message = f"Текущая загрузка CPU: {cpu_usage}%\nRAM: {mem}"
        response = send_telegram_alert(bot_token, chat_id, message)

        if response.status_code == 200:
            print("Алерт успешно отправлен!")
        else:
            print(f"Ошибка отправки алерта: {response.status_code}")

    # Пауза перед следующим измерением
    time.sleep(15)