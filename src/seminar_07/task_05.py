# 01:49:30
"""
Задание №5

Доработаем предыдущую задачу.

Создайте новую функцию которая генерирует файлы с разными расширениями.

Расширения и количество файлов функция принимает в качестве параметров.

Количество переданных расширений может быть любым.

Количество файлов для каждого расширения различно.

Внутри используйте вызов функции из прошлой задачи.
"""
# 01:56:00
from task_04 import make_files


def main_maker(extensions: dict):
    # def main_maker(**kwargs: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':

    data = {
        'bin': 2,
        'zip': 3,
    }

    main_maker(data)
