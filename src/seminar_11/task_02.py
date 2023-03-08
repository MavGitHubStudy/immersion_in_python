"""
Задача №2

Создайте класс Архив, который хранит пару свойств.
Например, число и строку.

При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов

list-архивы также являются свойствами экземпляра
"""


# 32:55 - 39:05
class Archive:
    instance = None

    # count_archive = []
    # text_archive = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # объект не создавали
            cls.instance = super().__new__(cls)
        else:
            # повторная копия
            cls.instance.count_arсhive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    count_archive = []
    text_archive = []

    def __init__(self, count, text):
        self.count = count
        self.text = text
        self.count_archive.append(self.count)
        self.text_archive.append(self.text)


def main():
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    d2 = Archive(2, 'b')
    # print(d2.text, d2.text_archive)


if __name__ == '__main__':
    main()
# 49:09
"""
a ['a']

Process finished with exit code 0

"""
