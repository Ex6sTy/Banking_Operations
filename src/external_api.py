import requests
from typing import Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с информацией о транзакции.
    :return: Сумма транзакции в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if not API_KEY:
        raise ValueError("API ключ не установлен в файле .env")

    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": API_KEY}

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()

    return response.json().get("result", 0.0)
