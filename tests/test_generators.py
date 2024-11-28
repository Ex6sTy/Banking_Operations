import pytest
from typing import List, Dict, Optional, Iterator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример транзакций для тестирования
transactions: List[Dict[str, Optional[Dict[str, str]]]] = [
    {
        "id": "1",
        "state": "EXECUTED",
        "date": "2021-09-01T12:00:00",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": "2",
        "state": "EXECUTED",
        "date": "2021-08-01T12:00:00",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


# Тесты для функции filter_by_currency
def test_filter_by_currency() -> None:
    """
    Тестирование фильтрации транзакций по заданной валюте.
    """
    usd_transactions: Iterator[Dict[str, Optional[Dict[str, str]]]] = filter_by_currency(transactions, "USD")
    result: List[Dict[str, Optional[Dict[str, str]]]] = list(usd_transactions)
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_match() -> None:
    """
    Проверка работы функции, если транзакции в заданной валюте отсутствуют.
    """
    eur_transactions: Iterator[Dict[str, Optional[Dict[str, str]]]] = filter_by_currency(transactions, "EUR")
    result: List[Dict[str, Optional[Dict[str, str]]]] = list(eur_transactions)
    assert len(result) == 0


def test_filter_by_currency_empty() -> None:
    """
    Проверка работы функции при пустом списке транзакций.
    """
    empty_transactions: List[Dict[str, Optional[Dict[str, str]]]] = []
    usd_transactions: Iterator[Dict[str, Optional[Dict[str, str]]]] = filter_by_currency(empty_transactions, "USD")
    result: List[Dict[str, Optional[Dict[str, str]]]] = list(usd_transactions)
    assert len(result) == 0


# Тесты для функции transaction_descriptions
def test_transaction_descriptions() -> None:
    """
    Проверка корректного возврата описаний транзакций.
    """
    descriptions: Iterator[str] = transaction_descriptions(transactions)
    result: List[str] = list(descriptions)
    assert len(result) == 2
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    """
    Проверка работы функции при пустом списке транзакций.
    """
    empty_transactions: List[Dict[str, Optional[Dict[str, str]]]] = []
    descriptions: Iterator[str] = transaction_descriptions(empty_transactions)
    result: List[str] = list(descriptions)
    assert len(result) == 0


# Тесты для генератора card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    """
    Проверка корректности генерации номеров карт в заданном диапазоне.
    """
    result: List[str] = list(card_number_generator(start, stop))
    assert result == expected
