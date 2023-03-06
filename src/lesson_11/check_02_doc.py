class MyClass:
    A = 42
    """About class"""

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b

    def method(self):
        """Documentation"""
        self.__doc__ = None


help(MyClass)
"""
Help on class MyClass in module __main__:

class MyClass(builtins.object)
 |  MyClass(a, b)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, a, b)
 |      self.__doc__ = None
 |  
 |  method(self)
 |      Documentation
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  A = 42


Process finished with exit code 0
"""
# 35:50
