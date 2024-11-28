from datetime import datetime

import pytest
from typing import List, Dict, Optional, Union
from src.processing import filter_by_state, sort_by_date


# Тесты для функции filter_by_state
def test_filter_by_state() -> None:
    """
    Тестирование фильтрации списка словарей по заданному статусу state.
    """
    operations: List[Dict[str, str]] = [
        {"id": "1", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result: List[Dict[str, str]] = filter_by_state(operations, state="EXECUTED")
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize("state, expected_length", [("EXECUTED", 2), ("CANCELED", 1), ("PENDING", 0)])
def test_filter_by_state_parametrized(state: str, expected_length: int) -> None:
    """
    Параметризация тестов для различных возможных значений статуса state.
    """
    operations: List[Dict[str, str]] = [
        {"id": "1", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result: List[Dict[str, str]] = filter_by_state(operations, state=state)
    assert len(result) == expected_length


# Тесты для функции sort_by_date
def test_sort_by_date_descending() -> None:
    """
    Тестирование сортировки списка словарей по датам в порядке убывания.
    """
    operations: List[Dict[str, str]] = [
        {"id": "1", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result: List[Dict[str, str]] = sort_by_date(operations)
    assert result[0]["date"] > result[-1]["date"]


def test_sort_by_date_ascending() -> None:
    """
    Тестирование сортировки списка словарей по датам в порядке возрастания.
    """
    operations: List[Dict[str, str]] = [
        {"id": "1", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result: List[Dict[str, str]] = sort_by_date(operations, descending=False)
    assert result[0]["date"] < result[-1]["date"]


def test_sort_by_date_same_dates() -> None:
    """
    Проверка корректности сортировки при одинаковых датах.
    """
    operations: List[Dict[str, str]] = [
        {"id": "1", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2021-09-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
    ]
    result: List[Dict[str, str]] = sort_by_date(operations)
    assert len(result) == 3


@pytest.mark.parametrize(
    "invalid_date_operations",
    [
        [{"id": "1", "state": "EXECUTED", "date": "invalid-date"}],  # Некорректный формат даты
        [{"id": "2", "state": "CANCELED", "date": None}],  # Отсутствует дата
    ],
)
def test_sort_by_date_invalid_format(invalid_date_operations: List[Dict[str, Optional[str]]]) -> None:
    """
    Тесты на работу функции с некорректными или нестандартными форматами дат.
    """
    with pytest.raises(Exception):  # Ожидаем общее исключение, так как сортировка может вызвать разные типы ошибок
        sort_by_date(invalid_date_operations)
