from datetime import datetime

import pandas as pd


def current_time_greeting() -> str: #  Входные данные - YYYY-MM-DD HH:MM:SS
    """ Функция приветствия пользователя в зависимости от времени суток """

    user_datetime = datetime.now()
    user_hour = user_datetime.hour

    if 0 <= user_hour < 6:
        result = "Доброй ночи"
    elif 6 <= user_hour < 12:
        result = "Доброе Утро"
    elif 12 <= user_hour < 18:
        result = "Добрый день"
    else:
        result = "Добрый вечер"

    return result


def get_slice_data(date_time: str, date_format: str = "%Y-%m-%d %H:%M:%S"):
    """ Пример вывода: "20.05.2020 12:30:30" -> 01.05.2020-20.05.2020 """

    dt = datetime.strptime(date_time, date_format)
    start_month = dt.replace(day=1)
    return [
        start_month.strftime("%d-%m_%Y"), dt.strftime("%d-%m_%Y")
    ]


def get_cut_from_excel(path_to_file: str, period_date: list):
    """ Чтение xlsx файла. """
    
    df = pd.read_excel(path_to_file)
    return df.to_dict(orient='records')


