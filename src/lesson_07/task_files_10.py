with open('test_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()  # возврат пустой строки
    print(f'Читаем второй раз\n{res}')
