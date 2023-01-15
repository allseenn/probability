# В ящике находится 10 красных, 5 черных, 5 зеленых шаров. Наудачу вынимают 6 шаров. 
# Какова вероятность, что вынуты 3 красных, 2 черных, 1 зеленый
from math import factorial
import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
probability = (combinations(10,3) * combinations(5,2) * combinations(5,1)) / combinations(20,6)

print(f"Вероятность вынуть 3 красных, 2 черных и 1 зеленый шар {probability*100:1.2f}%")