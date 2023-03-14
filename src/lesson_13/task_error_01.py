class UserException(Exception):  # Наше базовое исключение
    pass


class UserAgeError(UserException):  # Дочернее исключение по возрасту
    pass


class UserNameError(UserException):  # Дочернее исключение по имени
    pass
# 49:55
