"""
Right методы

Левый объект не находит нужный метод, поэтому правый объект
вызывает свой метод и возвращает новый экземпляр класса
"""


class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words)
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
print(s * text)  # TypeError: 'str' object cannot be interpreted as an integer
"""
text = 'Каждый охотник желает знать где сидит фазан'
s = ' (=^.^=) '
Каждый (=^.^=) охотник (=^.^=) желает (=^.^=) знать (=^.^=) где (=^.^=) сидит (=^.^=) фазан
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_11/task_methods_03.py", line 22, in <module>
    print(s * text)  # TypeError: 'str' object cannot be interpreted as an integer
TypeError: 'str' object cannot be interpreted as an integer

Process finished with exit code 1
"""
# 01:06:00
