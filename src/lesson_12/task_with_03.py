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

    def __exit__(self,
                 exc_type,  # тип ошибки
                 exc_val,  # текст, который хранится внутри ошибки
                 exc_tb  # текст трассировки
                 ):
        self.connection.commit()  # подтверждаем изменения
        self.connection.close()  # закрываем соединение
        self.cursor = self.connection = None  # переменные cursor и connection
        # заменяем на значение None


db = DB('sqlite.db')
with db as cur:  # AttributeError: __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values('Гвидо', 66);""")
# 30:45
