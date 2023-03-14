class UserException(Exception):  # Наше базовое исключение
    pass


class UserAgeError(UserException):  # Дочернее исключение по возрасту
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'Возраст пользователя должен быть целым int() или '
                f'вещественным float() больше нуля.\n'
                f'У вас тип {type(self.value)}, а значение {self.value}'
                )


class UserNameError(UserException):  # Дочернее исключение по имени
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = 'попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.upper:
            text = 'больше верхней'
        return (f'Имя пользователя {self.name} содержит {len(self.name)} '
                f'символа(ов).\nЭто {text} границы. Попадите в диапазон '
                f'({self.lower}, {self.upper}).'
                )
# 49:55
