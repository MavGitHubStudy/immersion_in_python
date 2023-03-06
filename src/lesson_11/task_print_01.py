class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


user = User('Спенглер')
print(user)
"""
<__main__.User object at 0x7f032cfe72b0>

Process finished with exit code 0
"""
# 37:27
