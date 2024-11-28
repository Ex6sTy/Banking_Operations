import pytest
import os
import time
import logging

LOG_FILE = "test_log.txt"

@pytest.fixture(autouse=True)
def cleanup_logs() -> None:
    # Закрыть все обработчики логгера, чтобы освободить файл
    logger = logging.getLogger()
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)

    # Убедиться, что файл закрыт перед его удалением
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
        except PermissionError:
            # Если файл занят, подождать немного и попробовать снова
            time.sleep(1)
            if os.path.exists(LOG_FILE):
                os.remove(LOG_FILE)


@log(filename=LOG_FILE)
def divide(a: float, b: float) -> float:
    return a / b

@log(filename=LOG_FILE)
def add(a: int, b: int) -> int:
    return a + b

# Тестирование успешного выполнения функции и записи лога в файл
def test_log_to_file() -> None:
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    result = add(2, 3)
    assert result == 5

    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()

    assert "add ok" in log_content

# Тестирование успешного выполнения функции с возникновением ошибки и записи в лог файл
def test_log_error_to_file() -> None:
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()

    assert "divide error: ZeroDivisionError" in log_content

# Очистка логов после каждого теста
@pytest.fixture(autouse=True)
def cleanup_logs() -> None:
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

