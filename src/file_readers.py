import pandas as pd
from typing import List, Dict, Any


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.
    """
    try:
        data = pd.read_csv(file_path)
        return data.to_dict(orient="records")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except pd.errors.EmptyDataError:
        return []


def read_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список словарей с транзакциями.
    """
    try:
        data = pd.read_excel(file_path)
        return data.to_dict(orient="records")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
