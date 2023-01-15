# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial
import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
a_probability = (combinations(13,4) * combinations(39,0)) / combinations(52,4)
b_probability = (combinations(4,1) * combinations(48,3)) / combinations(52,4)
print(f"Вероятность вытащить все четыре крести {a_probability*100:1.2f}%")
print(f"Вероятность вытащить 1 туза в 4 картах {b_probability*100:1.2f}%")