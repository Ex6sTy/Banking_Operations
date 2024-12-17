# Banking Operations Widget

## Цель проекта

Проект представляет собой виджет для работы с банковскими операциями клиента. Виджет позволяет фильтровать и сортировать банковские операции, а также получать необходимую информацию о транзакциях клиента по различным критериям. Основная цель - упростить работу с данными о банковских операциях и обеспечить удобный доступ к важной информации.

## Основные функции

### 1. Filter by State

Функция `filter_by_state` предназначена для фильтрации списка банковских операций по их состоянию. По умолчанию она возвращает все операции со статусом `'EXECUTED'`, но можно указать и другой статус для фильтрации.

Пример использования:

```
from src.processing import filter_by_state

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

filtered_operations = filter_by_state(operations, state='CANCELED')
print(filtered_operations)
```

### 2. Sort by Date

Функция sort_by_date предназначена для сортировки списка операций по дате. По умолчанию сортировка выполняется в порядке убывания, чтобы сначала отображать последние операции.

Пример использования:
```
from src.processing import sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sorted_operations = sort_by_date(operations)
print(sorted_operations)
```

### 3. Get Masked Card Number

Функция get_mask_card_number предназначена для получения замаскированного номера карты. Она принимает номер карты в виде целого числа и возвращает строку, в которой часть номера скрыта для обеспечения безопасности.

Пример использования:
```
from src.masks import get_mask_card_number

card_number = 1234567812345678
masked_card = get_mask_card_number(card_number)
print(masked_card)
```
### 4. Get Masked Account Number

Функция get_mask_account предназначена для получения замаскированного номера счета. Она принимает номер счета в виде целого числа и возвращает строку, в которой часть номера скрыта для обеспечения безопасности.

Пример использования:
```
from src.masks import get_mask_account

account_number = 987654321
masked_account = get_mask_account(account_number)
print(masked_account)
```

### 5. Mask Account or Card Data

Функция mask_account_card предназначена для маскировки как номера карты, так и номера счета. Она принимает строку с данными и возвращает строку, в которой часть информации скрыта для обеспечения безопасности.

Пример использования:
```
from src.widget import mask_account_card

data = "Account: 123456789, Card: 9876543212345678"
masked_data = mask_account_card(data)
print(masked_data)
```

### 6. Get Formatted Date

Функция get_date предназначена для обработки и форматирования строки с датой. Она принимает строку с датой и возвращает отформатированную строку для удобного отображения.

Пример использования:
```
from src.widget import get_date

date_str = "2023-12-31T23:59:59"
formatted_date = get_date(date_str)
print(formatted_date)
```

## Установка
### Клонируйте репозиторий:
```
git clone <URL репозитория>
```
### Перейдите в директорию проекта:
```
cd BankingOperationsWidget
```
### Установите зависимости:
```
pip install -r requirements.txt
```

## Использование

### Импортируйте необходимые функции из модулей processing, masks и widget:
```
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
```
### Используйте функции для фильтрации операций по состоянию, сортировки операций по дате, маскировки номеров карты и счета, а также для форматирования данных.

Пример:
```
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_operations = filter_by_state(operations, state='CANCELED')
sorted_operations = sort_by_date(filtered_operations)

print(sorted_operations)

card_number = 1234567812345678
masked_card = get_mask_card_number(card_number)
print(masked_card)

account_number = 987654321
masked_account = get_mask_account(account_number)
print(masked_account)

data = "Account: 123456789, Card: 9876543212345678"
masked_data = mask_account_card(data)
print(masked_data)

date_str = "2023-12-31T23:59:59"# Описание проекта
```
Основная программа (main): Предоставляет интерактивное меню для пользователя:

Чтение данных из JSON, CSV или Excel-файла.
Фильтрация по статусу операций (EXECUTED, CANCELED и т.д.).
Сортировка по дате и выбор рублевых операций.
Фильтрация по ключевому слову в описании.

## Возможности

### Фильтрация операций по состоянию
Используйте `filter_by_state`, чтобы получить список операций с заданным статусом, например, 'CANCELED' или 'EXECUTED'.

### Сортировка операций по дате
Функция `sort_by_date` позволяет быстро получить отсортированный список операций, что удобно для анализа последних транзакций клиента.

### Маскировка номера карты
Используйте `get_mask_card_number`, чтобы получить замаскированный номер карты, скрыв часть информации для обеспечения безопасности.

### Маскировка номера счета
Используйте `get_mask_account`, чтобы получить замаскированный номер счета, скрыв часть информации для обеспечения безопасности.

### Маскировка данных счета и карты
Используйте `mask_account_card`, чтобы замаскировать как номер карты, так и номер счета в переданной строке.

### Форматирование даты
Используйте `get_date`, чтобы получить отформатированную дату для удобного отображения.

### Конвертация валют
Модуль `external_api` добавляет функционал для конвертации сумм транзакций в рубли с использованием API.

- **convert_to_rub(transaction)**
  Конвертирует сумму транзакции в рубли. Если валюта операции не RUB, используется внешний API для получения курса и расчета суммы в рублях.

  **Пример использования:**
  ```python
  transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
  amount_in_rub = convert_to_rub(transaction)
  print(amount_in_rub)
  ```

## Новый Модуль: Генераторы Транзакций

Модуль `generators` предоставляет функции для эффективной работы с большими объемами данных о транзакциях.

### Функции модуля:

- **filter_by_currency(transactions, currency)**
  Фильтрует список транзакций по заданной валюте и возвращает итератор.
  
  **Пример использования:**
  ```python
  usd_transactions = filter_by_currency(transactions, "USD")
  for transaction in usd_transactions:
      print(transaction)
  ```

- **transaction_descriptions(transactions)**
  Генератор, который возвращает описание каждой транзакции.
  
  **Пример использования:**
  ```python
  descriptions = transaction_descriptions(transactions)
  for description in descriptions:
      print(description)
  ```

- **card_number_generator(start, stop)**
  Генератор, создающий номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
  
  **Пример использования:**
  ```python
  for card_number in card_number_generator(1, 5):
      print(card_number)
  ```
  
### Фильтрация и подсчет транзакций

- **filter_transactions_by_description(transactions, search_string):**
  Ищет транзакции по ключевому слову в описании с использованием регулярных выражений.

  **Пример использования:**
  ```python
  filtered = filter_transactions_by_description(transactions, "вклад")
  print(filtered)

- **count_transactions_by_category(transactions)**
- Подсчитывает количество операций в каждой категории на основе описания.
- **Пример использования**
   ```
   counts = count_transactions_by_category(transactions)
   print(counts)
   ```
## Логирование

В проекте настроено логирование для модулей `utils` и `masks`:

### Логирование модуля `utils`
- Логи записываются в файл `logs/utils.log`.
- Формат логов: метка времени, название модуля, уровень серьезности и сообщение.
- Логируются успешные операции и ошибки при чтении JSON-файлов.

### Логирование модуля `masks`
- Логи записываются в файл `logs/masks.log`.
- Формат логов: метка времени, название модуля, уровень серьезности и сообщение.
- Логируются успешные операции и ошибки при маскировке номеров карт и счетов.

## Новый функционал: Чтение данных из CSV и Excel

В проект добавлены функции для работы с финансовыми транзакциями из CSV- и Excel-файлов.

### Использование

- **Чтение CSV**
  Функция `read_csv(file_path)` читает данные из CSV-файла и возвращает список словарей.

  **Пример:**
  ```python
  transactions = read_csv("transactions.csv")
  print(transactions)
  ```

## Вклад в проект
Проект разрабатывается с использованием подхода GitFlow. Основная разработка ведется в ветке `develop`, а функциональные изменения — в ветках с префиксом `feature`. Пожалуйста, убедитесь, что ваш код соответствует стандартам PEP 8 и имеет необходимые тесты, прежде чем создавать pull request.

# Информация о тестировании

Проект содержит тесты, которые обеспечивают проверку функциональности всех основных компонентов. Тестирование выполнено с использованием библиотеки `pytest`. Ниже описаны основные компоненты тестирования:

- **`mask_account_card`**: Проверяет правильность маскировки номера карты или счета. Также тестирует обработку некорректных данных, чтобы удостовериться в надежности функции.
- **`get_date`**: Проверяет преобразование строки с датой в требуемый формат ДД.ММ.ГГГГ. Также выполняются тесты для проверки обработки неверных форматов и отсутствующих дат.
- **`convert_to_rub`**: Проверяет корректность конвертации валют с использованием Mock и API.
- **`read_json`**: Проверяет успешное чтение JSON-файлов, обработку пустых файлов и некорректного формата данных.

## Запуск тестов
Для запуска тестов используйте команду:

```bash
pytest
```

Эта команда выполнит все тесты в проекте и отобразит результаты. Тесты находятся в директории `tests/` и покрывают все основные функции проекта, обеспечивая их корректное выполнение и обработку ошибок.

## Покрытие тестами
Тестирование включает различные случаи использования, в том числе граничные и нестандартные случаи, что помогает убедиться в правильности работы функций и устойчивости к неверным входным данным.

## Лицензия
Проект распространяется под лицензией MIT. Ознакомьтесь с файлом LICENSE для получения дополнительной информации.