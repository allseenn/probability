# В партии 10 деталей. Среди них 3 бракованные. Какова вероятность, 
# что среди 5 ,взятых на удачу, 4 хорошие детали?
from math import factorial
import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
probability = (combinations(7,4) * combinations(3,1)) / combinations(10,5)

print(f"Вероятность вытащить все четыре крести {probability*100:1.2f}%")
