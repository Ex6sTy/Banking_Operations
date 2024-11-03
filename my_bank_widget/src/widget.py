from masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param info: строка с типом и номером
    :return: строка с замаскированным номером.
    """
    parts = info.split(' ', 1)
    if len(parts) != 2:
        raise ValueError("Неверный формат входных данных")

    card_type, card_number = parts

    if card_type in ['Visa', 'MasterCard', 'Maestro']:
        return get_mask_card_number(card_number)
    elif card_type == "Счет":
        return get_mask_account(card_number)
    else:
        raise ValueError("Неизвестный тип карты или счета")

def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате ISO в строку формата "ДД.ММ.ГГГГ".

    :param date_string: строка с датой в  формате ISO (например, "2024-03-11T02:26:18.671407").
    :return: строка с датой в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime
    dt = datetime.fromisformat(date_string)
    return dt.strftime("%d.%m.%Y")
