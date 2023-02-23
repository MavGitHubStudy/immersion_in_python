"""
Напишите функцию группового переименования файлов.
Она должна:

- принимать параметр желаемое конечное имя файлов. При переименовании в конце
  имени добавляется порядковый номер.

- принимать параметр количество цифр в порядковом номере.

- принимать параметр расширение исходного файла. Переименование должно работать
  только для этих файлов внутри каталога.

- принимать параметр расширение конченого файла.

- принимать диапазон сохраняемого оригинального имени. Например, для диапазона
  [3, 6] берутся буквы с 3 по 6 из исходного имени файла.  К ним прибавляется
  желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
# import os
from pathlib import Path


def group_renaming(
        final_name: str = "_test",
        number_of_digits: int = 2,
        original_extension: str = "txt",
        final_extension: str = "tst",
        scope: tuple = (0, None)
):
    p = Path(Path().cwd())
    count = 0
    for obj in p.iterdir():
        if obj.is_file():
            new_file = ""
            _name, _ext = obj.name.split('.')
            if _ext == original_extension:
                count += 1
                new_file = ''.join([
                    _name[scope[0]:scope[1]],
                    final_name,
                    str(count).rjust(number_of_digits, "0"),
                    '.',
                    final_extension
                ])
                # print(new_file)
                obj.rename(new_file)


if __name__ == '__main__':
    group_renaming(number_of_digits=4, scope=(0, 3))
