import json

from config import PATH_TO_EXCEL
from src.utils import (
    current_time_greeting,
    get_slice_data
)

def main_page(date_str: str) -> json:
    """ Функция принимает на вход строку с датой в формате
    YYYY-MM-DD HH:MM:SS
    и возвращает JSON ответ с данными """

    time_period = get_slice_data(date_str)
    data_frame_cut = get_cut_from_excel(PATH_TO_EXCEL, time_period)

    # 1. Приветствие
    greeting = current_time_greeting()

    # 2. По каждой карте

    result = {
        "greeting": greeting,
        "cards": [],
        "top_transactions": [],
        "currency_rates": [],
        "stock_prices": []
    }

    return result
