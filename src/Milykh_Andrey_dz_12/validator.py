from abc import ABC, abstractmethod


class Validator(ABC):
    """Класс Validator является одновременно абстрактным
    базовым классом и дескриптором управляемого атрибута"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner=None):
        return getattr(instance, self.param_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.param_name, value)

    @abstractmethod
    def validate(self, value):
        pass
