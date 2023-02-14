data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}  # {None: 12}
res2 = (item for item in data if item > 4)  # <generator object <genexpr> at 0x7f3d285c0f90>
res3 = [[item] for item in data if item > 4]  # [[6], [8], [10], [12]]
print(res1, res2, res3)
"""
{None: 12} <generator object <genexpr> at 0x7f3d285c0f90> [[6], [8], [10], [12]]

Process finished with exit code 0
"""