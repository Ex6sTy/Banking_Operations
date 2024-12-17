from typing import Any, Dict, List

import pandas as pd


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях.
    """
    try:
        data = pd.read_csv(file_path, delimiter=";")  # Указан разделитель ';'
        if data.empty:
            return []
        return data.to_dict(orient="records")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except pd.errors.EmptyDataError:
        return []  # Если файл пустой, возвращаем пустой список
    except pd.errors.ParserError as e:
        raise ValueError(f"Ошибка парсинга CSV-файла {file_path}: {e}")


def read_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях.
    """
    try:
        data = pd.read_excel(file_path)
        return data.to_dict(orient="records")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except ValueError as e:
        raise ValueError(f"Ошибка парсинга Excel-файла {file_path}: {e}")
