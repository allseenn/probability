# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, 
# из второго - 4. Какова вероятность того, что 3 мяча белые?
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

probability = combinations(5,2)*combinations(3,0)/combinations(8,2) * combinations(5,1)*combinations(7,3)/combinations(12,4) \
            + combinations(5,1)*combinations(3,1)/combinations(8,2) * combinations(5,2)*combinations(7,2)/combinations(12,4) \
            + combinations(5,0)*combinations(3,2)/combinations(8,2) * combinations(5,3)*combinations(7,1)/combinations(12,4)
print(f"Вероятность вытащить 3 белых из обоих ящиков {probability} или {probability*100:0.2f}%")