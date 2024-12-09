import json
import logging
import os
from typing import Any, Dict, List

# Создаем директорию для логов если она отсутсвует
os.makedirs("logs", exist_ok=True)

# Настройка логера
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)  # Уровень DEBUG

# Настройка handler
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Настройка formatter
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление handler к логеру
utils_logger.addHandler(file_handler)


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.
    Args:
        file_path (str): Путь к JSON-файлу.
    Returns:
        List[Dict[str, Any]]: Список словарей с данными.
    """
    try:
        utils_logger.info(f"Attempting to read JSON file: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                utils_logger.warning(f"File {file_path} does not contain a list.")
                return []
            utils_logger.info(f"Successfully read JSON file: {file_path}")
            return data
    except FileNotFoundError as e:
        utils_logger.error(f"File not found: {file_path}. Error: {e}")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error(f"Error decoding JSON file: {file_path}. Error: {e}")
        return []
