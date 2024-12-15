from src.file_readers import read_csv, read_excel
import pytest
from unittest.mock import patch
import pandas as pd
from pathlib import Path


def test_read_csv_valid_file():
    result = read_csv("data/transactions.csv")
    assert isinstance(result, list)
    assert len(result) > 0


def test_read_csv_empty_file(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")
    result = read_csv(str(empty_file))
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_mocked(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{"id": 1, "amount": 100, "currency": "USD"}])
    result = read_excel("data/transactions.xlsx")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_read_excel_valid_file():
    # Обновляем путь к реальному файлу
    result = read_excel("data/transactions_excel.xlsx")
    assert isinstance(result, list)
    assert len(result) > 0


def test_read_excel_empty_file(tmp_path: Path):
    temp_file = tmp_path / "empty.xlsx"
    pd.DataFrame().to_excel(temp_file, index=False)

    result = read_excel(str(temp_file))
    assert result == []


def test_read_excel_invalid_format(tmp_path: Path):
    temp_file = tmp_path / "invalid.xlsx"
    with open(temp_file, "w") as f:
        f.write("Invalid Content")

    with pytest.raises(ValueError):
        read_excel(str(temp_file))
