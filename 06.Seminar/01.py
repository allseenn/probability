# Задача 1 
# На препарате А положительный результат лечения наблюдается у 17 из 32 пациентов, 
# а на препарате В у 9 из 22. Построить 95% доверительный интервал для разности долей. 
# Обнаружены ли статистически значимые различия?
# task2
import numpy
p=26/54
z=1.96
s=numpy.sqrt(p*(1-p)*(1/32+1/22))
delta = 17/32 - 9/22
print(delta+z*s)
print(delta-z*s)