from masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    Args:
        data (str): Строка с типом и номером карты или счета.

    Returns:
        str: Строка с замаскированным номером.
    """
    if data.startswith('Счет'):
        number = data.split(' ')[1]
        masked_number = get_mask_account(int(number))
        return f"Счет **{masked_number}"
    else:
        number = data.split(' ')[-1]
        masked_number = get_mask_card_number(int(number))
        return f"{' '.join(data.split(' ')[:-1])} {masked_number}"

from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.

    Args:
        date_str (str): Строка с датой в формате "ГГГГ-ММ-ДДTчч:мм:сс.микросекунды".

    Returns:
        str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date = datetime.fromisoformat(date_str.split('T')[0])
    return date.strftime('%d.%m.%Y')

