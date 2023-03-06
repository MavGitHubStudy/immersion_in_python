class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        """Информация для пользователя"""
        return f'Экземпляр класса User c именем "{self.name}"'


user = User('Спенглер')
print(user)
"""
Экземпляр класса User c именем "Спенглер"

Process finished with exit code 0
"""
# 38:59
