import pytest
from src.masks import get_mask_card_number, get_mask_account

# Тесты для функции get_mask_card_number
def test_get_mask_card_number():
    """
    Тестирование правильности маскирования номера карты.
    """
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert get_mask_card_number(1111222233334444) == "1111 22** **** 4444"

@pytest.mark.parametrize("card_number, expected", [
    (1234567812345678, "1234 56** **** 5678"),
    (1111222233334444, "1111 22** **** 4444")
])
def test_get_mask_card_number_various_formats(card_number, expected):
    """
    Проверка работы функции на различных входных форматах номеров карт.
    """
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("invalid_card_number", [
    1234,  # Нестандартная длина номера карты
    "abcd567812345678",  # Содержит нецифровые символы
    None  # Отсутствует номер карты
])
def test_get_mask_card_number_invalid(invalid_card_number):
    """
    Проверка, что функция корректно обрабатывает неверные входные данные.
    """
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(invalid_card_number)

# Тесты для функции get_mask_account
def test_get_mask_account():
    """
    Тестирование правильности маскирования номера счета.
    """
    assert get_mask_account(987654321) == "**4321"
    assert get_mask_account(123456789) == "**6789"

@pytest.mark.parametrize("account_number, expected", [
    (987654321, "**4321"),
    (123456789, "**6789")
])
def test_get_mask_account_various_formats(account_number, expected):
    """
    Проверка работы функции с различными форматами и длинами номеров счетов.
    """
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("invalid_account_number", [
    123,  # Номер счета меньше ожидаемой длины
    "abcd5678",  # Содержит нецифровые символы
    None  # Отсутствует номер счета
])
def test_get_mask_account_invalid(invalid_account_number):
    """
    Проверка, что функция корректно обрабатывает неверные входные данные.
    """
    with pytest.raises(ValueError, match="Номер счета должен содержать как минимум 4 цифры."):
        get_mask_account(invalid_account_number)
