# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, 
# что 2 приобретенных билета окажутся выигрышными?
import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
# Вероятность выиграть 2 выигрышных билета, это соотношение количество сочетаний вытащить 2 из двух
# И (умножить) количество сочетаний не вытащить ни огдного выигрышного 0 из 98
# Деленное на количество сочетаний всех возможных комбинаций выташить 2 билета из 100
probability = combinations(2,2) * combinations(98,0) / combinations(100,2)
print(f"Вероятность купить два выигрышных билета {probability*100:0.2f}%")