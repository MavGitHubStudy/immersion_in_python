def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the
    division in the range[2, P).
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)

# Запустим код в консоли в режиме интерпретатора Python
"""
/home/.../.venv/bin/python /home/.../src/lesson_14/test_doctest_01.py 
Help on function is_prime in module __main__:

is_prime(p: int) -> bool
    Checks the number P for simplicity using finding the remainder of the
    division in the range[2, P).


Process finished with exit code 0
"""
