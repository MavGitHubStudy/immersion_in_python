data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')


data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]  # 80 или 120 символов
print(f'{res = }')
"""
res = [2, 42, 76, 24]
res = [2, 42, 76, 24]

Process finished with exit code 0
"""
