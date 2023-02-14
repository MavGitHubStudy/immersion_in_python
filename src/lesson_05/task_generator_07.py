my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
for char in my_setcomp:
    print(char)


x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
"""
{'r', 'z', 'e', 'w', 'q', 'd', 'v', 'c', 'm', 'n', 'j', 'a', 'h', 'y', 's', 'x', 'k', 'p', 'b', 'o', 'u', 't', 'i', 'l', 'f', 'g'}
r
z
e
w
q
d
v
c
m
n
j
a
h
y
s
x
k
p
b
o
u
t
i
l
f
g
len(x)=7	len(y)=6
len(res)=19
{3, 5, 133, 7, 9, 11, 15, 19, 25, 27, 29, 37, 721, 723, 725, 733, 121, 123, 125}

Process finished with exit code 0
"""
