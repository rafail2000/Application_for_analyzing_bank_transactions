import datetime
import pandas as pd

from src.utils import get_time_tree_month


def main_reports(transactions: pd.DataFrame, category: str, date: str = datetime.datetime.today()):
    """Функция принимает на вход:
    датафрейм с транзакциями,
    название категории,
    опциональную дату.
    Если дата не передана, то берется текущая дата.
    """

    time_period = get_time_tree_month(date)

    start_date = pd.to_datetime(time_period[0], dayfirst=True)
    end_date = pd.to_datetime(time_period[1], dayfirst=True)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    filtered_transactions = transactions[transactions["Дата операции"].between(start_date, end_date)]
    filtered_df_on_category = filtered_transactions[filtered_transactions["Категория"] == category]

    return filtered_df_on_category
