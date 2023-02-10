def add_two_def(a, b):
    return a + b


add_two_lambda = lambda a, b: a + b  # Никогда подобного не пишем!


print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))


my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value =}')
"""
45.14
45.14
s_key = [('four', 4), ('one', 1), ('ten', 10), ('three', 3), ('two', 2)]
s_value =[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('ten', 10)]
"""