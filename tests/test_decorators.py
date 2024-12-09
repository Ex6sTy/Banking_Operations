import logging
import os
import time

import pytest

from src.decorators import log

LOG_FILE = "test_log.txt"


@pytest.fixture(autouse=True)
def cleanup_logs() -> None:
    # Получаем все обработчики логгера root
    root_logger = logging.getLogger()
    handlers = root_logger.handlers[:]

    # Закрываем все обработчики, затем удаляем их
    for handler in handlers:
        handler.acquire()  # Получаем блокировку, чтобы исключить конкуренцию
        try:
            handler.close()
        finally:
            handler.release()  # Освобождаем блокировку
        root_logger.removeHandler(handler)

    # Пытаемся удалить файл несколько раз, если он занят
    for _ in range(3):
        try:
            if os.path.exists(LOG_FILE):
                os.remove(LOG_FILE)
            break  # Удаление прошло успешно, выходим из цикла
        except PermissionError:
            time.sleep(1)


@log(filename=LOG_FILE)
def divide(a: int, b: int) -> float:
    return a / b


def test_log_to_file() -> None:
    result = divide(10, 2)
    assert result == 5.0
    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()
    assert "divide ok" in log_content


def test_log_error_to_file() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()
    assert "divide error: ZeroDivisionError" in log_content
