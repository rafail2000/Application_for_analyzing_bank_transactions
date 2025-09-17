from freezegun import freeze_time

from src.utils import current_time_greeting


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
