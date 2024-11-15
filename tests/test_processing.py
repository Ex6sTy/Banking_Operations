from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date


# Тесты для функции filter_by_state
def test_filter_by_state():
    """
    Тестирование фильтрации списка словарей по заданному статусу state.
    """
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result = filter_by_state(operations, state="EXECUTED")
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize("state, expected_length", [("EXECUTED", 2), ("CANCELED", 1), ("PENDING", 0)])
def test_filter_by_state_parametrized(state, expected_length):
    """
    Параметризация тестов для различных возможных значений статуса state.
    """
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result = filter_by_state(operations, state=state)
    assert len(result) == expected_length


# Тесты для функции sort_by_date
def test_sort_by_date_descending():
    """
    Тестирование сортировки списка словарей по датам в порядке убывания.
    """
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result = sort_by_date(operations)
    assert result[0]["date"] > result[-1]["date"]


def test_sort_by_date_ascending():
    """
    Тестирование сортировки списка словарей по датам в порядке возрастания.
    """
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-08-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2021-07-01T12:00:00"},
    ]
    result = sort_by_date(operations, descending=False)
    assert result[0]["date"] < result[-1]["date"]


def test_sort_by_date_same_dates():
    """
    Проверка корректности сортировки при одинаковых датах.
    """
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-09-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2021-09-01T12:00:00"},
    ]
    result = sort_by_date(operations)
    assert len(result) == 3
