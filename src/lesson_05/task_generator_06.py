x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')
"""
len(x)=7	len(y)=6
len(res)=25
[3, 7, 25, 121, 721, 3, 7, 25, 121, 721, 5, 9, 27, 123, 723, 7, 11, 29, 125, 
 725, 15, 19, 37, 133, 733]
item = 3
item = 7
item = 25
...
item = 133
item = 733

Process finished with exit code 0
"""