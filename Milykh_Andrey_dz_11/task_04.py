"""
Задача №4

Доработаем класс Архив из задачи 2.

Добавьте методы представления экземпляра для программиста
и для пользователя.
"""
# 01:06:40


class Archive:
    """
    При первом запуске создаёт экземпляр класса, при повторном - добавляет
    в архив прежние данные.
    """
    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # cls.instance.count_archive = []
            # cls.instance.text_archive = []
        else:
            cls.instance.count_archive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text
        # self.count_archive.append(self.count)
        # self.text_archive.append(self.text)
        # 50:07

    def __str__(self):
        return (f'Архив содержит следующий текст: {self.text_archive} '
                f'и числа {self.count_archive}')

    def __repr__(self):
        return f'{self.__dict__}\t{self.count_archive}\t{self.text_archive}'


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    print(f'{d1}')
    print(f'{d1 = }')
"""
a []
Архив содержит следующий текст: [] и числа []
d1 = {'count': 1, 'text': 'a'}	[]	[]

Process finished with exit code 0
"""
# 1:09:51
