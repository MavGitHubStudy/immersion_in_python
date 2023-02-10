"""map(function, iterable)"""
texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)
"""
привет здорова приветствую
"""