from src.utils import read_json


def test_utils_logging() -> None:
    """
    Проверка логирования в модуле utils.
    """
    read_json("non_existing_file.json")
    read_json("data/operations.json")
