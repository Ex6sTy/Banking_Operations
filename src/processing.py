from typing import List, Dict

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по заданному состоянию.

    :param operations: Список операций (словарей).
    :param state: Состояние, по которому требуется фильтровать (по умолчанию 'EXECUTED').
    :return: Список операций с заданным состоянием.
    """
    return [operation for operation in operations if operation.get('state') == state]


