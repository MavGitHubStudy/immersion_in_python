def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the
    division in the range[2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. '
              'Working...')
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
/home/.../immersion_in_python/src/lesson_14/test_doctest_04.py 
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
Trying:
    is_prime(3.14)
Expecting:
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
ok
Trying:
    is_prime(-100)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
ok
Trying:
    is_prime(1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
ok
Trying:
    is_prime(100_000_001)
Expecting:
    If the number P is prime, the check may take a long time. Working...
    False
ok
Trying:
    is_prime(100_000_007)
Expecting:
    If the number P is prime, the check may take a long time. Working...
    True
ok
1 items had no tests:
    __main__
1 items passed all tests:
   7 tests in __main__.is_prime
7 tests in 2 items.
7 passed and 0 failed.
Test passed.

Process finished with exit code 0
"""
