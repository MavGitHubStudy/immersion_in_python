my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp)
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
"""
{97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 
 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 
 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 
 119: 'w', 120: 'x', 121: 'y', 122: 'z'}
dict[97] = a
dict[98] = b
dict[99] = c
...
dict[121] = y
dict[122] = z

Process finished with exit code 0
"""