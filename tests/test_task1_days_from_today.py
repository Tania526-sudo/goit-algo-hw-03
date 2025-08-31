import pytest
from goit_algo_hw_03 import get_days_from_today
from datetime import datetime, timedelta


def test_days_past():
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    assert get_days_from_today(yesterday) == 1


def test_days_future():
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert get_days_from_today(tomorrow) == -1


def test_invalid_format():
    with pytest.raises(ValueError):
        get_days_from_today("2021/10/09")
