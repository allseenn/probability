import numpy as np
def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

print(combinations(36,4))