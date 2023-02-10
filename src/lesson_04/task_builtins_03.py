"""zip(*iterables, strict=False)"""
names = ["Иван",  "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')
"""
Иван заработал 125000.00 денег и премию 12500.00
Николай заработал 96000.00 денег и премию 24000.00
Пётр заработал 109000.00 денег и премию 14170.00
"""
