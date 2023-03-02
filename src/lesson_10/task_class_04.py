class Person:
    max_up = 3


p1 = Person()

print(f'{id(Person) = }')
print(f'{Person.max_up = } {type(Person.max_up) = } {id(Person.max_up) = }')

print(f'{id(p1) = }')
print(f'{p1.max_up = } {type(p1.max_up) = } {id(p1.max_up) = }')

"""
id(Person) = 94330789922144
Person.max_up = 3 type(Person.max_up) = <class 'int'> id(Person.max_up) = 140646340247856
id(p1) = 140646337723504
p1.max_up = 3 type(p1.max_up) = <class 'int'> id(p1.max_up) = 140646340247856

Process finished with exit code 0
"""
