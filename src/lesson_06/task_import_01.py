import sys

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')
"""
Содержимое переменной sys.path формируется динамически

PYTHONPATH - переменная с путями до мест
расположения модулей
"""
