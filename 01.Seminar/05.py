# На 5 одинаковых карточках написаны буквы Ч, А, Й ,К, А.
# Какова вероятность, что получится слова ЧАЙКА
# PN - Перестановки с повторениями = N! / N1! * N2! * N3!, где N = N1+N2+N3
import numpy as np
print(f"Вероятность слова ЧАЙКА из букв ЧАЙКА {1/np.math.factorial(5)/np.math.factorial(2)*100:0.2f}%")