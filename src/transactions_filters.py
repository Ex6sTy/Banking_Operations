import re
from collections import Counter
from typing import Dict, List


def filter_transactions_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Фильтрует список операций по наличию строки поиска в описании операции.

    Args:
        transactions (List[Dict]): Список словарей с транзакциями.
        search_str (str): Строка для поиска в описании.

    Returns:
        List[Dict]: Список словарей с транзакциями, содержащих строку поиска.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict]) -> Dict[str, int]:
    """
        Подсчитывает количество банковских операций по их категориям на основе описания.

    Args:
        transactions (List[Dict]): Список словарей с транзакциями.

    Returns:
        Dict[str, int]: Словарь с категориями и количеством операций.
    """
    descriptions = [tx.get("description", "").lower() for tx in transactions]
    return dict(Counter(descriptions))
