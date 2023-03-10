import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    # __exit__ может обрабатывать ошибки, но это тема следующей лекции
    def __exit__(self,
                 exc_type,  # тип ошибки, если произойдёт
                 exc_val,  # текст, который хранится внутри ошибки
                 exc_tb  # текст трассировки, т.е. весь набор действий
                 # которые привели к данной ошибке
                 ):
        self.connection.commit()  # подтверждаем изменения
        self.connection.close()  # закрываем соединение
        self.cursor = self.connection = None  # переменные cursor и
        # connection заменяем на значение None, т.е. мы говорим, что мы ушли
        # в исходное состояние и можем работать с базой данных много раз,
        # используя один и тот же экземпляр, а если у нас несколько баз, то
        # создаём несколько экземпляров по одному для каждой базы и работаем
        # c ними


db = DB('sqlite.db')
with db as cur:  # AttributeError: __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
"""
/home/.../lesson_12/task_with_03.py 

Process finished with exit code 0
"""
# # 30:47 - 31:51
