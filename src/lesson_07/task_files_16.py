text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)  # res - сколько байт записано
    print(f'{res = }\n{len(text) = }')
