

class User:  # object
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман')
print('Создаём третий раз')
u_3 = User(name='Стэнц')
"""
Создаём первый раз
Создал класс <class '__main__.User'>
Создал self.name = 'Спенглер'
Создаём второй раз
Создал класс <class '__main__.User'>
Создал self.name = 'Венкман'
Создаём третий раз
Создал класс <class '__main__.User'>
Создал self.name = 'Стэнц'

Process finished with exit code 0
"""
# 11:57
