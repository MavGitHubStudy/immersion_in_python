data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)  # <dict_itemiterator objec
y = next(x)
print(y)  # ('один', 1)
z = next(iter(y))
print(z)  # один
"""
<dict_itemiterator object at 0x7f0ee94cb1f0>
('один', 1)
один

Process finished with exit code 0
"""
# 36:30
