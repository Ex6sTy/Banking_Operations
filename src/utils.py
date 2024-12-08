import json
from typing import List, Dict, Any


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями. Пустой список, если файл пустой, содержит некорректные данные или не найден.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
