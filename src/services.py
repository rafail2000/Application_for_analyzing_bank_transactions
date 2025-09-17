import json

from config import PATH_TO_EXCEL
from src.utils import get_slice_data_for_month, get_cut_from_excel, get_cashback


def main_services(year: str, month: str) -> json:
    """ Функция принимает на вход:
    data — данные с транзакциями;
    year — год, за который проводится анализ;
    month — месяц, за который проводится анализ.
    Выходные параметры:
    JSON
    {
    "Категория 1": 1000,
    "Категория 2": 2000,
    "Категория 3": 500
    }
    """

    time_period = get_slice_data_for_month(year, month)
    data_frame_cut = get_cut_from_excel(PATH_TO_EXCEL, time_period)
    cashback = get_cashback(data_frame_cut)

    return json.dumps(cashback, indent=4, ensure_ascii=False)
