import unittest


class TestCaseName(unittest.TestCase):

    def test_method(self):
        self.assertEqual(2 * 2, 5, msg='Видимо в этой вселенной не работает '
                                       ':-('
                         )


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_unittest_01.py 
test_method (__main__.TestCaseName) ... FAIL

======================================================================
FAIL: test_method (__main__.TestCaseName)
----------------------------------------------------------------------
Traceback (most recent call last):
  File 
"/home/novichkov/work/gb/immersion_in_python/src/lesson_14/test_unittest_01.py",
 line 7, in test_method
    self.assertEqual(2 * 2, 5, msg='Видимо в этой вселенной не работает '
AssertionError: 4 != 5 : Видимо в этой вселенной не работает :-(

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

Process finished with exit code 1
"""