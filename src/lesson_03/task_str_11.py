text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))  # 0 - начало поиска
# -5 - конец поиска (конец это -1)

text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text = :>25}')
