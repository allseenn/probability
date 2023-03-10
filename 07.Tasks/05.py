# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному 
# закону распределения. Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
import numpy as np
import scipy.stats as stats

a = 0.05
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
data.sort()
n=len(data)
m0 = 2.5
m1 = np.mean(data)
s = np.std(data, ddof=1)
t_e = (m1-m0)*10**0.5/s
t = stats.t.ppf(1-a, n-1)
print(f"t-наблюдаемое {t_e:.3f} не заходит за границы правостороннего критического значения\n\
t-табличного {t:.3f} Следовательно, нулевая гипотеза не опровергнута и значимых статистических\n\
различий между m1 {m1} и m0 {m0} нет.\n\
Партия изготавливается со средним арифметическим 2.5")