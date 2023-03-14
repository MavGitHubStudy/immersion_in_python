d = {'42': 73}
try:
    key, value = input('Ключ и значение: ').split()
    if d[key] == value:
        r = 'Совпадение'
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
else:
    print(r)
finally:
    print(d)
# 30:19
"""
>>> Ключ и значение: 42 13
>>> Ключ и значение: 42 13 3
>>> Ключ и значение: 73 42
>>> Ключ и значение: 42 73
"""
