import numpy as np
def arrangements(n,k):
    return np.math.factorial(n) // np.math.factorial(n-k)

print(arrangements(20,5))