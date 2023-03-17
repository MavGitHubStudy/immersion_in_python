def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the
    division in the range[2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    # doctest.testmod()  # testmod() - функция, запускающая тесты внутри файла
    doctest.testmod(verbose=True)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_doctest_02.py 

Process finished with exit code 0
"""
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_doctest_02.py 
Trying:
    is_prime(42)
Expecting:
    False
ok
Trying:
    is_prime(73)
Expecting:
    True
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.is_prime
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

Process finished with exit code 0
"""
