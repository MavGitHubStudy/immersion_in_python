"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть
10 самых частых. Не учитывать знаки препинания и регистр символов. За основу
возьмите любую статью из википедии или из документации к языку.
"""
import string

d = {}
some_string = """Тестовая строка, Строка, стРока, тестовая, количество 
встречаемых слов в которой необходимо вернуть, Количество: верНуть, 
Необходимо - интересно!"""
words = some_string.lower().split()
# print(words)
for i in range(len(words)):
    words[i] = words[i].strip(string.punctuation)
# print(words)
while "" in set(words):
    words.remove("")
print(words)
for


# for word in words:
#     word.strip(',.!?-')
# print(words)
