import numpy as np

a = np.array([10, 20, 30, 40, 50,])
print(np.mean(a))
print(np.var(a))
print(np.std(a))
b = (a - np.mean(a))/np.std(a)
print(b)
