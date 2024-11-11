from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по заданному состоянию.

    :param operations: Список операций (словарей).
    :param state: Состояние, по которому требуется фильтровать (по умолчанию 'EXECUTED').
    :return: Список операций с заданным состоянием.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param operations: Список операций (словарей).
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=descending)
