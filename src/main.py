import sys
from typing import Dict, List
from src.utils import read_json
from src.file_readers import read_csv, read_excel
from src.transactions_filters import count_transactions_by_category, filter_transactions_by_description


def display_transactions(transactions: List[Dict]) -> None:
    """
    Выводит транзакции на экран в читаемом формате.

    Args:
        transactions (List[Dict]): Список транзакций.
    """
    for tx in transactions:
        date = tx.get("date", "Не указана")
        description = tx.get("description", "Нет описания")
        amount = tx.get("operationAmount", {}).get("amount", "Не указано")
        currency = tx.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
        print(f"{date} - {description} - {amount} {currency}")


def main() -> None:
    """
    Основная функция программы для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите источник данных:")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. Excel-файл")

    file_type = input("Ваш выбор: ").strip()
    transactions = []
    try:
        if file_type == "1":
            transactions = read_json("data/transactions.json")
        elif file_type == "2":
            transactions = read_csv("data/transactions.csv")
        elif file_type == "3":
            transactions = read_excel("data/transactions_excel.xlsx")
        else:
            print("Неверный выбор. Завершение программы.")
            sys.exit(1)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    print(f"Загружено {len(transactions)} транзакций.")
    status = input("Введите статус транзакции (EXECUTED, CANCELED, PENDING): ").upper()
    filtered_transactions = [tx for tx in transactions if tx.get("state", "").upper() == status]

    print(f"Транзакции со статусом {status}:")
    display_transactions(filtered_transactions)

    search_str = input("Введите строку для поиска в описании операций: ").strip()
    search_results = filter_transactions_by_description(filtered_transactions, search_str)
    print(f"Найдено {len(search_results)} транзакций по строке '{search_str}':")
    display_transactions(search_results)

    categories = count_transactions_by_category(filtered_transactions)
    print("Подсчет операций по категориям:")
    for category, count in categories.items():
        print(f"{category}: {count} операций")
