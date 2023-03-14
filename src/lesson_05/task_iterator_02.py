data = [2, 4, 6, 8]
# list_iter = iter(data, 6)  # TypeError: iter(v, w): v must be callable

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):  # b'' - закончить
    # итерацию, когда будет получит пустой блок байт
    print(block)
f.close()
"""
/home/novichkov/work/gb/immersion_in_python/src/lesson_05/task_iterator_02.py 
b'Hello world!\nHow'
b' are you?\nCall m'
b'e later, please.'
b'\n'

Process finished with exit code 0
"""
# Даже там, где '\n' - это просто '\n' (Linux), обрабатывается он как
# переход к началу следующей строки.
#
# В терминалах платформ DOS/Windows символ \n всегда означал переход на
# следующую строку с сохранением горизонтальной позиции курсора. То есть
# в терминах "пишущей машинки" это означало прокрутку валика и бумаги на одну
# строку вперед без изменения положения каретки.
#
# Другими словами текст "ABCDE\nFGHIJ\nKLMNOP" терминалом DOS/Windows будет
# выведен как
#
# Код
# ----------------------------------------------------------------------------
# ABCDE
#      FGHIJ
#           KLMNOP
#
# Вот именно для того, чтобы не только перевести строку, но еще и вернуть
# каретку на начало новой строки, нужен символ \r.
# Комбинация \r\n - это именно возврат каретки за которым следует перевод
# строки.
#
# Можно и наоборот, но как-то устоялось именно \r\n.
#