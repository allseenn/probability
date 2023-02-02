# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности 
# среднего роста родителей и детей.
# Интервальная оценка для разности средних арифметических по формуле Δ± 𝑡_(𝛼/2)∗ 𝑆_Δ , где Δ= (𝑋_1 ) ̅− (𝑋_2 ) ̅
# 𝑆_Δ=√(𝐷/𝑛_1 +𝐷/𝑛_2 ), где 𝑛_1 и  𝑛_2 – объемы выборок, общая дисперсия 𝐷=1/2(𝐷_1+𝐷_2), 
import numpy as np
import scipy.stats as stats
mom = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
kid = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
n = len(mom)
mom_mean = np.mean(mom)
kid_mean = np.mean(kid)
difference = mom_mean - kid_mean
d1 = np.var(mom, ddof=1)
d2 = np.var(kid, ddof=1)
a = 0.975
t = stats.t.ppf(a, 2*(n-1))
D = (d1+d2)/2
SE = np.sqrt(D/n+D/n)
print(f"Средний рост родителей {mom_mean} и детей {kid_mean}, их разница {difference:.2f}")
print(f"95% доверительный интервал для разности среднего роста родителей и детей {difference-t*SE:.2f} {difference+t*SE:.2f}")