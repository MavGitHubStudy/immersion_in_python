"""
Задача №2

Создайте класс Архив, который хранит пару свойств.
Например, число и строку.

При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов

list-архивы также являются свойствами экземпляра
"""


class Archive:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            pass
        return cls.instance

    count_archive = []
    text_archive = []

    def __init__(self, count, text):
        self.count = count
        self.text = text
        self.count_archive.append(self.count)
        self.text_archive.append(self.text)


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
