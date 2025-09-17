import pytest


@pytest.fixture
def night_time():
    return "2025-09-08 00:30:30"


@pytest.fixture
def morning_time():
    return "2025-09-08 06:30:30"


@pytest.fixture
def day_time():
    return "2025-09-08 12:30:30"


@pytest.fixture
def evening_time():
    return "2025-09-08 18:30:30"
