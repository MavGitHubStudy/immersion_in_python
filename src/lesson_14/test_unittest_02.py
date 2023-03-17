import io
import unittest
from unittest.mock import patch

from prime_unittest import is_prime


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(42))
        self.assertFalse(is_prime(73))

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_flags(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take '
                         'a long time. Working...\n'
                         )

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take '
                         'a long time. Working...\n'
                         )


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_unittest_02.py 
test_is_prime (__main__.TestPrime) ... ok
test_type (__main__.TestPrime) ... ok
test_value (__main__.TestPrime) ... ok
test_warning_flags (__main__.TestPrime) ... ok
test_warning_true (__main__.TestPrime) ... ok

----------------------------------------------------------------------
Ran 5 tests in 6.269s

OK

Process finished with exit code 0
"""
# Error
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_unittest_02.py 
test_is_prime (__main__.TestPrime) ... ok
test_type (__main__.TestPrime) ... ok
test_value (__main__.TestPrime) ... ok
test_warning_flags (__main__.TestPrime) ... FAIL
test_warning_true (__main__.TestPrime) ... FAIL

======================================================================
FAIL: test_warning_flags (__main__.TestPrime)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/mock.py", line 1369, in patched
    return func(*newargs, **newkeywargs)
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_14/test_unittest_02.py", line 25, in test_warning_flags
    self.assertEqual(mock_stdout.getvalue(),
AssertionError: 'If the number P is prime, the check may take a long time. Working..\n' != 'If the number P is prime, the check may take a long time. Working...\n'
- If the number P is prime, the check may take a long time. Working..
+ If the number P is prime, the check may take a long time. Working...
?                                                                    +


======================================================================
FAIL: test_warning_true (__main__.TestPrime)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/mock.py", line 1369, in patched
    return func(*newargs, **newkeywargs)
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_14/test_unittest_02.py", line 33, in test_warning_true
    self.assertEqual(mock_stdout.getvalue(),
AssertionError: 'If the number P is prime, the check may take a long time. Working..\n' != 'If the number P is prime, the check may take a long time. Working...\n'
- If the number P is prime, the check may take a long time. Working..
+ If the number P is prime, the check may take a long time. Working...
?                                                                    +


----------------------------------------------------------------------
Ran 5 tests in 6.405s

FAILED (failures=2)

Process finished with exit code 1

"""