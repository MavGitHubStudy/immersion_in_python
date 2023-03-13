def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
"""
File "/home/.../src/lesson_13/task_intro_03.py", line 5
    return num
    ^^^^^^
SyntaxError: expected 'except' or 'finally' block

Process finished with exit code 1
"""
