import pytest
from src.widget import mask_account_card, get_date
from typing import Optional

# Тесты для функции mask_account_card
@pytest.mark.parametrize("data, expected", [
    ("Счет 123456789", "Счет ****6789"),
    ("Карта Visa 1234567812345678", "Карта Visa 1234 56** **** 5678"),
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444")
])
def test_mask_account_card(data: str, expected: str) -> None:
    """
    Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных.
    """
    assert mask_account_card(data) == expected

@pytest.mark.parametrize("data", [
    "Счет abcd5678",  # Некорректный формат номера счета
    "Карта Visa abcd5678",  # Некорректный формат номера карты
    "",  # Пустая строка
    None  # None вместо строки
])
def test_mask_account_card_invalid(data: Optional[str]) -> None:
    """
    Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
    """
    with pytest.raises((ValueError, AttributeError, TypeError)):  # Ожидаем ValueError, AttributeError или TypeError
        mask_account_card(data)

# Тесты для функции get_date
@pytest.mark.parametrize("date_str, expected", [
    ("2021-09-01T12:00:00.000000", "01.09.2021"),
    ("2022-01-15T05:30:45.123456", "15.01.2022")
])
def test_get_date(date_str: str, expected: str) -> None:
    """
    Тестирование правильности преобразования даты.
    """
    assert get_date(date_str) == expected

@pytest.mark.parametrize("date_str", [
    "invalid-date",  # Некорректный формат даты
    ""  # Пустая строка
])
def test_get_date_invalid(date_str: str) -> None:
    """
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата или формат неверен.
    """
    with pytest.raises((ValueError, TypeError, AssertionError)):  # Ожидаем ValueError, TypeError или AssertionError
        get_date(date_str)
