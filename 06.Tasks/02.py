# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
# значение с доверительной вероятностью 0,95.
#
# Найдем доверительный интервал для средних арифметических по формуле 𝑥 ̅±𝑡_(𝛼/2) * 𝜎/√𝑛, т.к. 
# СКО - генеральной совокупности неизвестно
import scipy.stats as stats
import numpy as np
data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
data.sort()
a = 1- 0.95
n=10
sigma = np.std(data, ddof=1)
x = np.mean(data)
t = stats.t.ppf( a / 2, n-1)
print(f"Доверительный интервал для средних арефметических {x+t*sigma/np.sqrt(n):.2f} {x-t*sigma/np.sqrt(n):.2f}")