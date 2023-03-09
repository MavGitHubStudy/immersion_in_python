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


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
    d3 = Archive(3, 'c')
    print(d3.text, d3.text_archive)
"""
 []
b ['a']
c ['a', 'b']

Process finished with exit code 0
"""
# 50:31
