from src.transactions_filters import count_transactions_by_category, filter_transactions_by_description

transactions = [
    {"description": "Открытие вклада", "state": "EXECUTED"},
    {"description": "Перевод на карту", "state": "CANCELED"},
    {"description": "Открытие вклада", "state": "EXECUTED"},
]


def test_filter_transactions_by_description():
    result = filter_transactions_by_description(transactions, "вклада")
    assert len(result) == 2
    assert all("вклада" in tx["description"].lower() for tx in result)


def test_count_transactions_by_category():
    result = count_transactions_by_category(transactions)
    assert result == {"открытие вклада": 2, "перевод на карту": 1}
