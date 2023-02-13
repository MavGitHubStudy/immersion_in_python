"""
Напишите функцию, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ - значение
переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое
представление.
"""


def key_arguments(**kwargs):
    d = {}
    for k, v in kwargs.items():
        if isinstance(v, list | dict | set | bytearray):
            d[str(v)] = k
        else:
            d[v] = k
    return d


source_d = {'par1': 1,
            'par2': 0.2,
            'par3': 'test',
            'par4': [1, 2, 3],
            'par5': {'one': 1, 'two': 2, 'three': 3},
            }

print(source_d)
res = key_arguments(**source_d)
print(res)

b = bytearray(b'hello world')
print(key_arguments(par6=10, par7=b))
