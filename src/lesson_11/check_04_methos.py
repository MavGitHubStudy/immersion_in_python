class MyClass:

    def __init__(self, data):
        self.data = data

    def __and__(self, other):
        return MyClass(self.data + other.data)

    def __str__(self):
        return str(self.data)


def main():
    a = MyClass((1, 2, 3, 4, 5))
    b = MyClass((2, 4, 6, 8, 10))
    print(a & b)


if __name__ == '__main__':
    main()
"""
(1, 2, 3, 4, 5, 2, 4, 6, 8, 10)

Process finished with exit code 0
"""
# 01:13:30
