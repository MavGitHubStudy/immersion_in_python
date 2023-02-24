import pickle
import os

# 58:55
res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')

os.system('echo Hello world!')
"""
Hello world!
res = 0
Hello world!

Process finished with exit code 0
"""
