# Ниже приведены диаметры коронарных артерий после приема нифедипина и плацебо. Позволяют 
# ли приводимые ниже данные утверждать, что нифедипин влияет на диаметр коронарных артерий?
# 1. Выполнить расчеты в Python
# 2. Сделайте расчет в ручную
# 3. Сравните критерий Стьюдента и p-value со значениями, полученными в Python
import scipy.stats as stats
import numpy as np
##### Вариант 1 расчета ##########
# x - после нифедипина
x = np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8,2.4, 2.3, 2.7, 2.7, 1.9])
# y - после плацебо
y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])
# Используем функцию ttest_ind (independent) для независимых случайных величин
print(stats.ttest_ind(x, y))
# statistic=1.328 - t_emp наблюдаемое , p-value=0.1999 больше alpha=0.05 -> H0 не опровергается

######### Вариант 2 ########################
a = 0.05
# t_emp (эмпирическое) наблюдаемое
t_emp = (np.mean(x) - np.mean(y)) / np.sqrt(np.var(x, ddof=1)/len(x)+np.var(y, ddof=1)/len(y))
# левая критическая область
t1 = stats.t.ppf(a / 2, df=2 * (len(x)-1))
# Правая критическая область 
t2 = stats.t.ppf(1 - a / 2, df=2 * (len(y)-1))
# t наблюдаемое лежит между критическими значениями -> H0 не опровергается
print(f"{t1} < {t_emp} < {t2}")

# d1 = np.var(x, ddof=1)
# d0 = np.var(y, ddof=1)
# m1 = np.mean(x)
# m0 = np.mean(y)
# D = (d1 + d0) / 2
# print((m1-m0)/np.sqrt(2*D/len(x)))