# 1:29:35
"""
Задание №6

Доработайте задачу 5.

Вынесите общие свойства и методы классов в класс
Животное.

Остальные классы наследуйте от него.

Убедитесь, что в созданные ранее классы внесены правки.
"""


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

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, name, age):
        self.is_flies = is_flies
        super().__init__(name, age)  # name и age уходят
        # в родительский класс для инициализации

    def can_flies(self):
        return f'The bird {self.name} flies? {self.is_flies}!'

    # def __str__(self):
    #     # ...
    #     spam = 'летает' if self.is_flies else 'ходит'
    #     return (  # обязательный возврат строки
    #         f'Перед нами птица по имени {self.name}. '
    #         f'Ей {self.age}  лет. Эта птица {spam}.'
    #     )


class Dog(Animal):
    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):  # 1:42:31
        if self.height < 0.5:
            return f'{self.name} маленький питомец'
        elif 0.5 < self.height < 1:
            return f'{self.name} обычная собака'
        return f'Wow! The dog {self.name} is {self.height} meters tall! BIG!'


# 1:30:50
if __name__ == '__main__':
    f = Fish('лососевый', 'Рыбец', 3)
    print(f.name)
    print(f.get_color())

    # 1:36:35
    b = Bird(True, 'Ворон', 146)
    print(b.can_flies())  # 1:40:05
    print(b)  # 1:54:00

    d = Dog(0.3, 'Рекс', 1)
    print(d.get_height())  # 1:43:40

