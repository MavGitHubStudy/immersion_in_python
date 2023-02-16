"""
Напишите однострочный генератор словаря, который принимает на вход три списка
одинаковой длины: имена str, ставка int, премия str с указанием процентов
вида "10.25%". В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается как ставка умноженная на
процент премии
"""
import decimal
from typing import List, Dict

PERC = 100


def dict_maker(str_names: List[str],
               int_list: List[int],
               percents: List[str]
               ) -> Dict[str, decimal.Decimal]:
    res_dict = {}
    for name, val, perc in zip(str_names, int_list, percents):
        res_dict[name] = val + (val * decimal.Decimal(perc[:-1])) / PERC

    yield res_dict


res = dict_maker(['Andy', 'Garry', 'Bob'], [20, 50, 200], ['10.25%', '12.5%',
                                                           '3.85%'])
print(*res)
