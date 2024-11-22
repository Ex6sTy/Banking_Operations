import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Пример данных транзакций
@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


# Тесты для функции filter_by_currency
def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_match(transactions):
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)
    assert len(result) == 0


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


# Тесты для функции transaction_descriptions
def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)
    assert result == ["Перевод организации", "Перевод со счета на счет"]


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert len(result) == 0


# Тесты для генератора card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_empty():
    result = list(card_number_generator(5, 4))
    assert len(result) == 0
