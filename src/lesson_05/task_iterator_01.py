"""iter(object[, sentinel])"""
# 24:00

a = 42
# iter(a)  # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)  # уже ничего не выводится!
"""
<list_iterator object at 0x7f6c1bf4c1f0>
2 4 6 8


Process finished with exit code 0
"""
