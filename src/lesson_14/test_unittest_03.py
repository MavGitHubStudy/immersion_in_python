import doctest
import unittest

import prime


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_unittest_03.py 
is_prime (prime)
Doctest: prime.is_prime ... ok
/home/.../immersion_in_python/src/lesson_14/prime.md
Doctest: prime.md ... ok

----------------------------------------------------------------------
Ran 2 tests in 12.865s

OK

Process finished with exit code 0
"""