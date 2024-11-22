from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
        Фильтрует список транзакций по заданной валюте.

        Args:
            transactions (List[Dict]): Список транзакций.
            currency (str): Валюта для фильтрации (например, 'USD').

        Yields:
            Dict: Транзакция с заданной валютой.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание транзакций.

    Args:
        transactions (List[Dict]): Список транзакций.

    Yields:
        str: Описание транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, создающий номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): Начальное значение для генерации.
        stop (int): Конечное значение для генерации.

    Yields:
        str: Сгенерированный номер карты в заданном диапазоне.
    """
    for num in range(start, stop + 1):
        yield f"{num:016}".replace("", " ")[1:-1]