from src.utils import get_time_tree_month


def test_get_time_tree_month(get_data):
    """ Тест возвращение трёх месячнего периода """

    assert get_time_tree_month(get_data) == ['01.06.2021', '01.09.2021']