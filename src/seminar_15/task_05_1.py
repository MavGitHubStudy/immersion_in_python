"""1:30:00 - 1:36:20 task_05.py"""
import argparse
import logging
from datetime import datetime
"""
Задание №5

Дорабатываем задачу 4.

Добавьте возможность запуска из командной строки.

При этом значение любого параметра можно опустить. В этом
случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.

*Научите функцию распознавать не только текстовые 
названия дня недели и месяца, но и числовые,
т.е. не мая, а 5.
"""
FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO,
                    filename='logs_5.log',
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


# 1:38:55
def parser_func():
    parser = argparse.ArgumentParser(description='Получаем дату datetime из '
                                                 'строки')
    parser.add_argument('--count', default='1')
    parser.add_argument('--weekday', default=datetime.now().weekday())
    parser.add_argument('--month', default=datetime.now().month)
    args = parser.parse_args()  # 1:43:40
    print(args)

    weekday = WEEKDAYS[args.weekday] if isinstance(
        args.weekday, int) else args.weekday

    month = MONTHS[args.month] if isinstance(
        args.month, int) else args.month

    return get_date(f'{args.count} {weekday} {month}')  # 1:55:20


if __name__ == "__main__":
    # print(get_date('3-я среда мая'))  # 1:25:32
    # print(get_date('1-й четверг ноября'))
    # # понедельник - 0, ..., воскресенье - 6
    # print(datetime.now().weekday())  # 1:18:24
    # parser_func()  # 1:43:40
    print(parser_func())
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
"""
# 1:42:00
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
python task_05.py --help
2023-05-17 00:00:00
2023-11-02 00:00:00
2
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
"""
# 1:45:20
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
python task_05.py --count 1-й --weekday четверг --month ноября
Namespace(count='1-й', weekday='четверг', month='ноября')
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
"""
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
python task_05_1.py --count 1-й --month ноября
Namespace(count='1-й', weekday=2, month='ноября')
2023-11-01 00:00:00
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $
"""
# 1:56:00
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
python task_05_1.py --count 1-й
Namespace(count='1-й', weekday=2, month=3)
2023-03-01 00:00:00
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/seminar_15: (main) $ 
"""
