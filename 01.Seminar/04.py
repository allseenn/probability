# На 5 одинаковых карточках написаны буквы Ч, А, Й ,К, И
# Какова вероятность, что получится слова ЧАЙКИ
from math import factorial
import numpy as np
def permutations(n):
    return np.math.factorial(n)

print(f"Вероятность написать ЧАЙКИ из букв ЧАЙКИ {1/permutations(5)*100:0.2f}%")