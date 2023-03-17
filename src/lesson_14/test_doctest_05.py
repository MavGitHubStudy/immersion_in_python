import doctest

doctest.testfile('prime.md', verbose=True)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_doctest_05.py 
Trying:
    from prime import is_prime
Expecting nothing
ok
Trying:
    is_prime(2)
Expecting:
    True
ok
Trying:
    is_prime(100000007)
Expecting:
    If the number P is prime, the check may take a long time. Working...
    True
ok
1 items passed all tests:
   3 tests in prime.md
3 tests in 1 items.
3 passed and 0 failed.
Test passed.

Process finished with exit code 0
"""
# 27:05
