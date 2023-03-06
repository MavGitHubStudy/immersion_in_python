"""
Задание №1

Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его
из класса-фабрики.
"""
from enum import Enum  # Модуль enum содержит в себе тип для перечисления
# значений с возможностью итерирования и сравнения.


class AnimalType(Enum):
    FISH = 0,
    BIRD = 1,
    DOG = 2


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):
    def __init__(self, color: str, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):
    def __init__(self, is_flies: bool, name, age):
        self.is_flies = is_flies
        super().__init__(name, age)  # name и age уходят
        # в родительский класс для инициализации

    def can_flies(self):
        return f'The bird {self.name} flies? {self.is_flies}!'


class Dog(Animal):
    def __init__(self, height: float, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height < 0.5:
            return f'{self.name} маленький питомец'
        elif 0.5 < self.height < 1:
            return f'{self.name} обычная собака'
        return f'Wow! The dog {self.name} is {self.height} meters tall! BIG!'


def make_animal(animal_type: AnimalType, *args) -> Animal:
    factory_dict = {
        AnimalType.FISH: Fish,
        AnimalType.BIRD: Bird,
        AnimalType.DOG: Dog
    }
    return factory_dict[animal_type](*args)


if __name__ == '__main__':
    # f = Fish('лососевый', 'Рыбец', 3)
    # print(f.name)
    # print(f.get_color())
    animal = make_animal(AnimalType.FISH, 'лососевый', 'Рыбец', 3)
    print(animal.name)
    if isinstance(animal, Fish):
        print(animal.get_color())

    # b = Bird(True, 'Ворон', 146)
    # print(f.name)
    # print(b.can_flies())
    # print(b)
    animal = make_animal(AnimalType.BIRD, True, 'Ворон', 146)
    print(animal.name)
    if isinstance(animal, Bird):
        print(animal.can_flies())

    # d = Dog(0.3, 'Рекс', 1)
    # print(f.name)
    # print(d.get_height())
    animal = make_animal(AnimalType.DOG, 0.3, 'Рекс', 1)
    print(animal.name)
    if isinstance(animal, Dog):
        print(animal.get_height())
