from src.views import welcome_script


def test_welcome_script(night_time, morning_time, day_time, evening_time):
    assert welcome_script(night_time) == "Доброй ночи"
    assert welcome_script(morning_time) == "Доброе Утро"
    assert welcome_script(day_time) == "Добрый день"
    assert welcome_script(evening_time) == "Добрый вечер"