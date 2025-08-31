from src.goit_algo_hw_03.task3_normalize_phone import normalize_phone


def test_with_plus():
    assert normalize_phone("+380501234567") == "+380501234567"


def test_without_plus():
    assert normalize_phone("380501234567") == "+380501234567"


def test_with_zero():
    assert normalize_phone("0501234567") == "+380501234567"


def test_with_symbols():
    assert normalize_phone("    +38(050)123-32-34") == "+380501233234"
