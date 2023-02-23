# 46:20
<<<<<<< HEAD
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus '
        'veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam '
        'velit?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())  # 0 - позиция в самом начале конец файла в 0 позиции
    for line in text:
        f.write(f'{line}\n')  # добавление строки
        print(f.tell())  # вернуть позицию конца файла
    print(f.tell())  # ещё раз убеждаемся, что курсор находится в конце
    # файла(205)
print(f.tell())  # ValueError: I/O operation on closed file.
# мы не можем определить позицию конца файла после того, как файл был закрыт
=======
>>>>>>> refs/remotes/origin/main
