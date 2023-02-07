my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))  # 2
print(my_dict.get('five'))  # None
print(my_dict.get('five', 5))  # 5 - default(значение по умолчанию)
print(my_dict.get('ten', 5))  # 10
