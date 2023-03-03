class DivStr(str):  # 01:33:00
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):  # магический метод
        first = self.obj.endswith('/')  # заканчивается ли первая половина
        # строки на символ деления '/' - Ture или False
        start = self.obj

        # цепочка проверок
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)

        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')  # /home/user - должно тоже работать !
path_2 = DivStr('my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')
"""
result = '/home/user/my_project/workdir', <class '__main__.DivStr'>
result / "text" = '/home/user/my_project/workdir/text'
result / 42 = '/home/user/my_project/workdir/42'
result * 3 = '/home/user/my_project/workdir/home/user/my_project/workdir/home/user/my_project/workdir'

Process finished with exit code 0
"""
