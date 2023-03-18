import pytest


@pytest.fixture
def data():
    return [2, 3, 5, 7]


def test_append(data):
    data.append(11)
    assert data == [2, 3, 5, 7, 11]


def test_remove(data):
    data.remove(5)
    assert data == [2, 3, 7]


def test_pop(data):
    data.pop()
    assert data == [2, 3, 5]


if __name__ == '__main__':
    # pytest.main(['-v'])  # -v  - аналог флага verbous=True
    # pytest.main(['test_pytest_03.py'])  # -v  - аналог флага verbous=True
    pytest.main(['-v', 'test_pytest_03.py'])
    # -v  - аналог флага verbous=True
"""
/home/..../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_pytest_03.py 
============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0 -- /home/novichkov/work/gb/immersion_in_python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/.../immersion_in_python/src/lesson_14
collecting ... collected 3 items

test_pytest_03.py::test_append PASSED                                    [ 33%]
test_pytest_03.py::test_remove PASSED                                    [ 66%]
test_pytest_03.py::test_pop PASSED                                       [100%]

============================== 3 passed in 0.02s ===============================

Process finished with exit code 0
"""
# 1:21:28
