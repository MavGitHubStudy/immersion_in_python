def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.

    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 73, 256, 0))
help(max_before_hundred)
"""
73
Help on function max_before_hundred in module __main__:

max_before_hundred(*args)
    Return the maximum number not exceeding 100.
    
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
"""