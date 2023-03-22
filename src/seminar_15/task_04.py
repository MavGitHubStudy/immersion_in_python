"""1:00:10 - 1:07:00 task_04.py"""
import logging
from datetime import datetime
"""
Задание №4

Функция получает на вход текст вида: "1-й четверг ноября",
"3-я среда мая" и т.п.

Преобразуйте его в дату в текущем году.

Логируйте ошибки, если текст не соответствует формату.
"""
FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO,
                    filename='logs_4.log',
                    encoding='utf-8',
                    format=FORMAT,
                    style='{')
logger = logging.getLogger(__name__)

# MONTHS = {'января': 1, 'февраля': 2, }
MONTHS = ('', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен',
          'окт', 'ноя', 'дек')
WEEKDAYS = ('по', 'вт', 'ср', 'че', 'пя', 'су', 'во')


def get_date(string: str) -> datetime:
    year = datetime.now().year

    count, weekday, month = string.split()
    month = MONTHS.index(month[:3])
    weekday = WEEKDAYS.index(weekday[:2])  # 1:21:08
    count = int(count[0])  # 1:22:30

    logger.info(f'{count}, {weekday}, {month}, {year}')
    spam_count = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == weekday:
            spam_count += 1
            if spam_count == count:
                return date


if __name__ == "__main__":
    print(get_date('3-я среда мая'))  # 1:25:32
    print(get_date('1-й четверг ноября'))
    # понедельник - 0, ..., воскресенье - 6
    print(datetime.now().weekday())  # 1:18:24
