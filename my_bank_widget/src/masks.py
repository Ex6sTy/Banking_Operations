def get_mask_card_number(card_number: int) -> str:
    """Возвращает замаскированный номер карты."""
    card_number_str = str(card_number)
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Возвращает замаскированный номер счета."""
    account_number_str = str(account_number)
    if len(account_number_str) < 4 or not account_number_str.isdigit():
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")

    masked_account_number = f"**{account_number_str[-4:]}"
    return masked_account_number
