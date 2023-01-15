import numpy as np
n = 360
np.random.seed(1)
c = np.random.randint(1,7, size = n)
d = np.random.randint(1,7, size = n)
a = c[(c == 1) & (d ==2)]
m = len(a)
W = m/n
print(W)