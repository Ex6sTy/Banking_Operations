import logging

# Настройка логирования для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)  # Установлен уровень DEBUG

# Настройка обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Настройка формата для логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты.

    Args:
        card_number (int): Номер карты.

    Returns:
        str: Замаскированный номер карты.
    """
    masks_logger.info(f"Masking card number: {card_number}")
    card_number_str = str(card_number)

    if len(card_number_str) != 16 or not card_number_str.isdigit():
        masks_logger.error("Invalid card number format.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
    masks_logger.info(f"Masked card number: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счета.

    Args:
        account_number (int): Номер счета.

    Returns:
        str: Замаскированный номер счета.
    """
    masks_logger.info(f"Masking account number: {account_number}")
    account_number_str = str(account_number)

    if len(account_number_str) < 4 or not account_number_str.isdigit():
        masks_logger.error("Invalid account number format.")
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")

    masked_account_number = f"**{account_number_str[-4:]}"
    masks_logger.info(f"Masked account number: {masked_account_number}")
    return masked_account_number
