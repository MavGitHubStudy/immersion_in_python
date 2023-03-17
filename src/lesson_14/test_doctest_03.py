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
/home/.../src/lesson_14/test_doctest_03.py 
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
**********************************************************************
File "/home/.../immersion_in_python/src/lesson_14/test_doctest_03.py", line 9, 
in __main__.is_prime
Failed example:
    is_prime(3.14)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
Got:
    Traceback (most recent call last):
      File "/usr/lib/python3.10/doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.is_prime[2]>", line 1, in <module>
        is_prime(3.14)
      File "/home/.../lesson_14/test_doctest_03.py", line 28, in is_prime
        for i in range(2, p):
    TypeError: 'float' object cannot be interpreted as an integer
Trying:
    is_prime(-100)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
**********************************************************************
File "/home/.../lesson_14/test_doctest_03.py", line 13, in __main__.is_prime
Failed example:
    is_prime(-100)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
Got:
    True
Trying:
    is_prime(1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
**********************************************************************
File "/home/.../lesson_14/test_doctest_03.py", line 17, in __main__.is_prime
Failed example:
    is_prime(1)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
Got:
    True
Trying:
    is_prime(100_000_001)
Expecting:
    If the number P is prime, the check may take a long time. Working...
    False
**********************************************************************
File "/home/.../src/lesson_14/test_doctest_03.py", line 21, in __main__.is_prime
Failed example:
    is_prime(100_000_001)
Expected:
    If the number P is prime, the check may take a long time. Working...
    False
Got:
    False
Trying:
    is_prime(100_000_007)
Expecting:
    If the number P is prime, the check may take a long time. Working...
    True
**********************************************************************
File "/home/.../lesson_14/test_doctest_03.py", line 24, in __main__.is_prime
Failed example:
    is_prime(100_000_007)
Expected:
    If the number P is prime, the check may take a long time. Working...
    True
Got:
    True
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   5 of   7 in __main__.is_prime
7 tests in 2 items.
2 passed and 5 failed.
***Test Failed*** 5 failures.

Process finished with exit code 0
"""
