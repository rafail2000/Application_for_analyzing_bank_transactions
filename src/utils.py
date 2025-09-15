import os
from datetime import datetime, timedelta

import pandas as pd
import requests
from dotenv import load_dotenv
import yfinance as yf


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
        start_month.strftime("%d.%m.%Y"), dt.strftime("%d.%m.%Y")
    ]


def get_cut_from_excel(path_to_file: str, period_date: list) -> list[dict]:
    """ Чтение xlsx файла и срез по дате """

    start_date = pd.to_datetime(period_date[0], dayfirst=True)
    end_date = pd.to_datetime(period_date[1], dayfirst=True)

    df = pd.read_excel(path_to_file)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    filtered_df = df[df["Дата операции"].between(start_date, end_date)]
    return filtered_df.to_dict(orient="records")


def get_total_spent_card(dataframe):
    """ Группировка по картам, вывод общее число расходов и кешбэк"""

    result = []
    cards = {}

    for i in dataframe:
        if i.get('Номер карты', False) not in cards:
            cards[i.get('Номер карты')] = [i.get('Сумма операции с округлением')]
        else:
            cards[i.get('Номер карты')].append(i.get('Сумма операции с округлением'))

    for key, value in cards.items():
        result.append({"last_digits": key, "total_spent": sum(value), "cashback": round(sum(value)/100, 2)})

    return result


def get_five_transaction(data_frame_cut):
    """ Получение пяти транзакций с максимальным платежом """

    result = []

    descending_sort = sorted(data_frame_cut, key=lambda x: x["Сумма операции с округлением"], reverse=True)

    for i in descending_sort[0:5]:
        result.append({"date": str(i["Дата операции"]),
                       "amount": i["Сумма операции с округлением"],
                       "category": i["Категория"],
                       "description": i["Описание"]
                       })

    return result


def get_exchange_rate():
    """ Получение курса валют """

    result = []

    load_dotenv()

    api_key = os.environ.get("API_KEY")

    data = requests.get(api_key).json()
    data_eur_usd = [data['Valute']['USD'], data['Valute']['EUR']]

    for i in data_eur_usd:
        result.append({"currency": i['CharCode'], "rate": round(i['Value'], 2)})

    return result


def get_share_price():
    """ Получение цены акций S&P 500"""

    company = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    result = []

    for i in company:
        com = yf.Ticker(i)
        info = com.info
        result.append({"stock": i, "price": info.get('postMarketPrice')})

    return result


def get_slice_data_for_month(year: str, month: str, date_format: str = "%Y-%m-%d") -> list:
    """ Пример вывода: "20.05.2020" -> 01.05.2020-31.05.2020 """

    date = f"01.{month}.{year}"
    start_month = datetime.strptime(date, "%d.%m.%Y")
    next_month = start_month.replace(day=28) + timedelta(days=4)
    end_month = next_month - timedelta(days=next_month.day)

    return [
        start_month.strftime("%d.%m.%Y"), end_month.strftime("%d.%m.%Y")
        ]

def get_cashback(data):
    """ Функция для вычисления выгодной категории кэшбэка """

    result = {}

    sorted_data = sorted(data, key=lambda x: x['Кэшбэк'], reverse=True)

    for i in sorted_data:
        result[i['Категория']] = i['Кэшбэк']

    return result