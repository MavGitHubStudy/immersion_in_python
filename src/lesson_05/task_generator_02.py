my_gen = (chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char)
"""
<generator object <genexpr> at 0x7f910ea3ceb0>
a
b
...

z

Process finished with exit code 0
"""