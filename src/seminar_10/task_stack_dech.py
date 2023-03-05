stack = list()
stack.append(2)
stack.append(3)
stack.append(6)
spam = stack.pop()
stack.append(7)
spam = stack.pop()
len(stack)


from collections import deque


d = deque()
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d[1] = 5  # получаем линейную асимптотику !!!
d[12345] = 5