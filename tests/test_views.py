from freezegun import freeze_time

from config import PATH_TO_EXCEL
from src.utils import current_time_greeting, get_slice_data, get_cut_from_excel, get_total_spent_card, \
    get_five_transaction


def test_current_time_greeting(night_time, morning_time, day_time, evening_time):
    """Тестирование с фиксированным временем """

    with freeze_time(night_time):
        assert current_time_greeting() == "Доброй ночи"

    with freeze_time(morning_time):
        assert current_time_greeting() == "Доброе Утро"

    with freeze_time(day_time):
        assert current_time_greeting() == "Добрый день"

    with freeze_time(evening_time):
        assert current_time_greeting() == "Добрый вечер"


def test_get_slice_data(night_time):
    """ Тест получения среза дат """

    assert get_slice_data(night_time) == ['01.09.2025', '08.09.2025']


def test_get_cut_from_excel(slice_date_none, slice_date):
    """ Тест получения среза из excel """

    assert get_cut_from_excel(PATH_TO_EXCEL, slice_date_none) == []


def test_get_total_spent_card(slice_data_excel):
    """ Тесты по самым высоким расходам по картам """

    assert get_total_spent_card(slice_data_excel) == [{'cashback': 72.73, 'last_digits': '*7197', 'total_spent': 7272.75},
 {'cashback': 3.45, 'last_digits': '*4556', 'total_spent': 345.0}]


def test_get_five_transaction(slice_data_excel):
    """ Тесты для проверки топ пяти транзакций """

    assert get_five_transaction(slice_data_excel) == [{'date': '2021-09-01 14:51:14', 'amount': 5990.0, 'category': 'Каршеринг', 'description': 'Ситидрайв'}, {'date': '2021-09-01 10:56:17', 'amount': 345.0, 'category': 'Аптеки', 'description': 'Аптека Вита'}, {'date': '2021-09-02 09:16:40', 'amount': 289.99, 'category': 'Супермаркеты', 'description': 'Магнит'}, {'date': '2021-09-01 18:28:48', 'amount': 246.45, 'category': 'Супермаркеты', 'description': 'Магнит'}, {'date': '2021-09-01 21:00:34', 'amount': 200.0, 'category': 'Местный транспорт', 'description': 'Метро Санкт-Петербург'}]
