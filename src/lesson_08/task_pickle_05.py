import pickle


def func(a, b, c):
    return a * b * c


with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')
"""
new_dict = {'numbers': [42, 4.1415, (7+3j)], 'functions': (<function func at 0x7f57055e4a60>, <built-in function sum>, <built-in function max>), 'others': {False, True, 'Hello world!'}}
new_dict["functions"][0](2, 3, 4) = 24

Process finished with exit code 0
"""
