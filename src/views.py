import json


from config import PATH_TO_EXCEL
from src.utils import (
    current_time_greeting,
    get_slice_data,
    get_cut_from_excel,
    get_total_spent_card,
    get_five_transaction,
    get_exchange_rate, get_share_price
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
    group_cards = get_total_spent_card(data_frame_cut)

    # 3. Топ-5 транзакций по сумме платежа
    top_five_transaction = get_five_transaction(data_frame_cut)

    # 4. Курс валют
    exchange_rate = get_exchange_rate()

    # 5. Стоимость акций из S&P500
    share_price = get_share_price()

    result = {
        "greeting": greeting,
        "cards": group_cards,
        "top_transactions": top_five_transaction,
        "currency_rates": exchange_rate,
        "stock_prices": share_price
    }

    return json.dumps(result, indent=4, ensure_ascii=False)
