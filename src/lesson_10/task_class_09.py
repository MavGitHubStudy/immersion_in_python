class Person:  # 25:55
    max_up = 3

    def __init__(self):  # self - не зарезервированное слово !
        self.level = 1
        self.health = 100
        print(f'{id(self) = }')


p1 = Person()
print(f'{id(p1) = }')
p2 = Person()
print(f'{id(p2) = }')
"""
id(self) = 140413477208560
id(p1) = 140413477208560
id(self) = 140413479137968
id(p2) = 140413479137968

Process finished with exit code 0
"""
