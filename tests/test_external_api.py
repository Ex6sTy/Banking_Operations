from unittest.mock import patch

from src.external_api import convert_to_rub
from src.utils import read_json


def test_read_json_valid_file():
    transactions = read_json("data/operations.json")
    assert isinstance(transactions, list)
    assert len(transactions) > 0


def test_read_json_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("[]")
    transactions = read_json(str(file_path))
    assert transactions == []


def test_read_json_invalid_format(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{}")
    transactions = read_json(str(file_path))
    assert transactions == []


def test_convert_to_rub_usd_to_rub():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 7500.0}
        result = convert_to_rub(transaction)
        assert result == 7500.0


def test_convert_to_rub_rub_currency():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction)
    assert result == 100.0
