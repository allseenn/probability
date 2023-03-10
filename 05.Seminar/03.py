# Утверждается, что средний рост мужчин национальности Х 179,5.
# Была взята выборка из 100 человек, по которой получилось среднее арифметическое 178,5. 
# Проверить это утверждение с помощью одностороннего теста, если известно, 
# что стандартное отклонение генеральной совокупности 3 см. 
# А уровень статистической значимости принять за 1%
import scipy.stats as stats
m0 = 179.5
m1 = 178.5
n = 100
a = 0.01
s = 3
z = (m1-m0) / (s/n**0.5)
z1 = stats.norm.ppf(a)
# z наблюдаемое меньше z табличного (критичного) -> следовательно H0 опровергается
print(f"{z} < {z1}")