"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
даты на проверку.

Задание №7

- Создайте модуль и напишите в нём функцию, которая
  получает на вход дату в формате DD.MM.YYYY
- Функция возвращает истину, если дата может существовать
  или ложь, если такая дата невозможна.
- Для простоты договоримся, что год может быть в диапазоне
  [1, 9999].
- Весь период (1 января 1 года - 31 декабря 9999 года)
  действует Григорианский календарь.
- Проверку года на високосность вынести в отдельную
  защищённую функцию.
"""


def check_date(date: str) -> bool:
    MIN_YEAR = 1
    MAX_YEAR = 9999

    if date[0] == '-':
        return False
    _list_date = date.split('.')
    _day, _month, _year = _list_date[0], _list_date[1], _list_date[2]
    num_day = int(_day)
    num_month = int(_month)
    num_year = int(_year)

    if num_year < MIN_YEAR or num_year > MAX_YEAR:
        return False
    if num_month < 1 or num_month > 12:
        return False
    # если январь, март, май, июль, август, октябрь, декабрь (31 день в месяце)
    if num_month in [1, 3, 5, 7, 8, 10, 12] and (num_day < 1 or num_day > 31):
        return False
    # если апрель, июнь, сентябрь, ноябрь (30 дней в месяце)
    if num_month in [4, 6, 9, 11] and (num_day < 1 or num_day > 30):
        return False
    if num_month == 2:  # если февраль
        if _check_leap(num_year):  # если год високосный
            if num_day < 1 or num_day > 29:
                return False
        else:  # если год обычный
            if num_day < 1 or num_day > 28:
                return False

    return True


def _check_leap(year: int) -> bool:
    SMALL_YEAR = 4
    MIDDLE_YEAR = 100
    BIG_YEAR = 400
    # GREG_YEAR = 1582

    # year = int(input('Введите год в формате yyyy: '))
    # if year < GREG_YEAR:
    #    result = "Григорианский календарь ещё не существует"
    if year % BIG_YEAR == 0:
        return True  # Високосный год
    elif year % MIDDLE_YEAR == 0:
        return False  # Обычный год
    elif year % SMALL_YEAR == 0:
        return True  # Високосный год
    else:
        return False  # Обычный год


if __name__ == "__main__":
    print(check_date("20.02.0000"))
    print(check_date("20.02.2023"))
    print(check_date("20.02.10000"))
    print(check_date("13.19.1970"))
    print(check_date("29.02.2024"))
    print(check_date("34.02.2024"))
    print(check_date("31.11.2024"))
