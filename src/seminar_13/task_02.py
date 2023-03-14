"""
task_02.py  (11:33)
"""
"""
Задание №2

- Создайте функцию аналог get для словаря
- Помимо самого словаря функция при принимает ключ и 
  значение по умолчанию.
- При обращении к несуществующему ключу функция должна
  возвращать дефолтное значение.
- Реализуйте работу через обработку исключений.
"""


def get(dct: dict, key, val=None):
    try:
        result = dct[key]
    except KeyError as e:
        print(f'{e = }')
        result = val
    return result


if __name__ == '__main__':
    d = {1: 1, 2: 2, 3: 3}
    # 17:43
    # print(get(d, 1, 'Hi'))
    """
    1
    
    Process finished with exit code 0
    """
    # 17:58
    print(get(d, 5, 'Hi'))
    """
    /home/.../.venv/bin/python /home/.../src/seminar_13/task_02.py 
    Traceback (most recent call last):
      File "/home/.../src/seminar_13/task_02.py", line 22, in <module>
        print(get(d, 5, 'Hi'))
      File "/home/.../src/seminar_13/task_02.py", line 15, in get
        result = dct[key]
    KeyError: 5
    
    Process finished with exit code 1    
    """
