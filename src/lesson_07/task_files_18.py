text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus '
        'veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam '
        'velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')
# Заглянем в файл new_data.txt. Внутри файла одна строка теста.
