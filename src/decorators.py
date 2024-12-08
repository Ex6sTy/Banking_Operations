import logging
import functools
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функций.

    Логирует начало и конец выполнения функции, ее результат или возникшие ошибки.
    Может записывать логи в указанный файл или выводить их в консоль.

    Args:
        filename (Optional[str]): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция, логирующая свое выполнение.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)

            # Добавляем обработчик, только если он еще не был добавлен
            if not logger.handlers:
                logger.addHandler(handler)

            try:
                logger.info(f"Calling function: {func.__name__} with args: {args} kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                # Закрываем обработчик, чтобы освободить файл или поток
                handler.close()
                logger.removeHandler(handler)

        return wrapper

    return decorator
