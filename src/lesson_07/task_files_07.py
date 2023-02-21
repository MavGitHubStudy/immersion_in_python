# Старый стиль: Python версии 3.9 и более ранние
with open('test_data.txt', 'r+', encoding='utf-8') as f1, \
        open('bin_data', 'rb') as f2, \
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') \
        as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))
