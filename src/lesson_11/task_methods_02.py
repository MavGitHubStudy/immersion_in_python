# 58:47
from random import choices


class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки',
               'туфли')

    def __init__(self, count: int, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'Осталось вещей в шкафу {self.count}:\n{names}'

    def __rshift__(self, other):
        """>>"""
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))


cl = Closet(10)
print(cl)
for _ in range(4):
    cl = cl >> 3
    print(cl)
"""
Осталось вещей в шкафу 10:
рубашка, брюки, носки, костюм, туфли, перчатки, рубашка, носки, носки, футболка
Осталось вещей в шкафу 7:
рубашка, рубашка, носки, костюм, носки, рубашка, рубашка
Осталось вещей в шкафу 4:
рубашка, рубашка, рубашка, носки
Осталось вещей в шкафу 1:
рубашка
Осталось вещей в шкафу 0:


Process finished with exit code 0
"""
# 01:01:10
