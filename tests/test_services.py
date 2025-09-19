from src.utils import get_slice_data_for_month, get_cashback


def test_get_slice_data_for_month(get_year_month):
    """ Тест дат месяца """

    assert get_slice_data_for_month(*get_year_month) == ['01.10.2020', '31.10.2020']


def test_get_cashback(slice_data_excel):
    """ Тесты по возврату кэшбэка """

    assert get_cashback(slice_data_excel) == {'Аптеки': 3.0}