"""
Представление для создания экземпляра, __repr__

Строка должна создать новый экземпляр, если скопировать её в код.
"""
class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user = User('Спенглер')
print(user)
"""
User(Спенглер)

Process finished with exit code 0
"""
