# 1:16:08
"""
Задание №5

Создайте три(или более) отдельных классов животных.
Например рыбы, птицы, т т.п.

У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.

Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""
# 1:26:00


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_unique(self):
        pass


class Fish(Animal):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)


class Bird(Animal):
    def __init__(self, is_flies, *args):
        self.is_filies = is_flies
        super().__init__(*args)


class Dog(Animal):
    def __init(self, height, *args):
        self.height = height
        super().__init__(*args)
