class MyStr(str):
    def __init__(self, value, author):
        self.author = author
        super().__init__(value)


def main():
    s = MyStr('Hello world!', 'prepod')


if __name__ == '__main__':
    main()
"""
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/seminar_11/task_01_2.py", line 12, in <module>
    main()
  File "/home/novichkov/work/gb/immersion_in_python/src/seminar_11/task_01_2.py", line 8, in main
    s = MyStr('Hello world!', 'prepod')
TypeError: decoding str is not supported

Process finished with exit code 1
"""
# 30:00
