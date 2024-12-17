from typing import Dict, List, Optional

import pytest


# Тесты для функции filter_by_state
def test_filter_by_state() -> None:
    # добавлены аннотации для возвращаемого значения
    ...


@pytest.mark.parametrize("state, expected_length", [("EXECUTED", 2), ("CANCELED", 1), ("PENDING", 0)])
def test_filter_by_state_parametrized(state: str, expected_length: int) -> None:
    # добавлены аннотации для аргументов и возвращаемого значения
    ...


# Тесты для функции sort_by_date
def test_sort_by_date_descending() -> None: ...


def test_sort_by_date_ascending() -> None: ...


def test_sort_by_date_same_dates() -> None: ...


@pytest.mark.parametrize(
    "invalid_date_operations",
    [[{"id": 1, "state": "EXECUTED", "date": "invalid-date"}], [{"id": 2, "state": "CANCELED", "date": None}]],
)
def test_sort_by_date_invalid_format(invalid_date_operations: List[Dict[str, Optional[str]]]) -> None: ...
