# Найти ско СВ Х, распределенной по биномиальному закону с параметрами n=50, p=0.6
# standard_deviation σ = √npq
import math
n = 50
p = 0.6
q = 1 - p
standard_deviation = math.sqrt(n*p*q)
print(f"Среднеквадратичное отклонение СКО случайной величины СВ равно {standard_deviation}")