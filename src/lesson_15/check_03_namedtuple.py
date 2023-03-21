from collections import namedtuple

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics',
                           'genetics'], defaults=[5, 5, 5, 5])

d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data(),
}
print(d)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/check_03_namedtuple.py 
{'Ivanov': Data(mathematics=4, chemistry=5, physics=3, genetics=5), 
'Petrov': Data(mathematics=5, chemistry=5, physics=4, genetics=3), 
'Sidorov': Data(mathematics=5, chemistry=5, physics=5, genetics=5)}

Process finished with exit code 0
"""
# 1:07:00
