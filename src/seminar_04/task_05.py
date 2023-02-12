"""
Задание №5

Функция принимает на сход три списка одинаковой длины:
- имена str,
- ставка int,
- премия str с указанием процентов вида "10.25%".

Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.

Сумма рассчитывается, как ставка, умноженная на процент
премии.
"""
import decimal

PERC = 100


def dict_maker(str_names: list[str],
               int_list: list[int],
               percents: list[str]
               ) -> dict[str, decimal.Decimal]:
    res_dict = {}
    for name, val, perc in zip(str_names, int_list, percents):
        res_dict[name] = val + (val * decimal.Decimal(perc[:-1])) / PERC

    return res_dict


res = dict_maker(['Andy', 'Garry', 'Bob'], [20, 50, 200], ['10.25%', '12.5%',
                                                           '3.85%'])
print(res)
