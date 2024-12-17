import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Константы для работы с API
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

    # Если валюта уже RUB, возвращаем сумму
    if currency == "RUB":
        return amount

    # Проверка наличия API ключа
    if not API_KEY:
        raise ValueError("API ключ не установлен в файле .env")

    # Параметры и заголовки запроса
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": API_KEY}

    # Отправка запроса к API
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()

    # Получение результата конверсии
    return response.json().get("result", 0.0)
