"""
closure[ˈkləʊʒə] - замыкание
"""
# 14:33
from typing import Callable


def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}

    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d

    return loc


small = main(42)
big = main(73)
print(small(7), big(7), small(3))
"""
{0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744} 
{0: 1, 1: 73, 2: 5329, 3: 389017, 4: 28398241, 5: 2073071593, 6: 151334226289}
{0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
"""
