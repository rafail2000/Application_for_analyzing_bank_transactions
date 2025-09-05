import datetime

def welcome_script(date: str) -> str: #  Входные данные - YYYY-MM-DD HH:MM:SS
    """ Функция приветствия пользователя """

    current_time = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    current_hour = current_time.hour

    if 0 <= current_hour < 6:
        result = "Доброй ночи"
    elif 6 <= current_hour < 12:
        result = "Доброе Утро"
    elif 12 <= current_hour < 18:
        result = "Добрый день"
    else:
        result = "Добрый вечер"

    return result
