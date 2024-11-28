import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func:Callable) -> Callable:
        # Настройка логгера
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f'Calling function: {func.__name__} with args: {args} kwargs: {kwargs}')
                result = func(*args, **kwargs)
                logger.info(f'{func.__name__} ok')
                return result
            except Exception as e:
                logger.error(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}')
                raise

        return wrapper
    return decorator
