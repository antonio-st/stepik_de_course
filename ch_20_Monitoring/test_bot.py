import requests


def send_telegram_alert(token, chat_id, message):
    """
    Отправка сообщения в Telegram.

    :param token: токен вашего бота (str)
    :param chat_id: ID чата, куда нужно отправить сообщение (str)
    :param message: Текст сообщения, которое нужно отправить (str)
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"  # Возможность отправки сообщений с HTML разметкой
    }
    response = requests.post(url, data=payload)
    return response


if __name__ == "__main__":
    # Вставьте сюда ваш токен и ID чата
    bot_token = "7840843505:AAFMj2fq5sL2qv1PPZBsAog6BM51cAPt8vI"
    chat_id = "213407163"

    # Сообщение для отправки
    message = "Это тестовое сообщение из Python!"

    # Отправка сообщения
    response = send_telegram_alert(bot_token, chat_id, message)

    if response.status_code == 200:
        print("Сообщение успешно отправлено!")
    else:
        print(f"Ошибка отправки сообщения: {response.status_code}")