# В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 
# Какова вероятность того, что ровно два мяча белые? 
# Какова вероятность того, что хотя бы один мяч белый?
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def bernulli(n,p,k):
    return combinations(n,k)*p**k*(1-p)**(n-k)

# Вероятность вытащить 2 белых из первого И 2 белых из второго ящика
probability = combinations(7,2)*combinations(3,0)/combinations(10,2) * combinations(9,2)*combinations(2,0)/combinations(11,2)
print(f"1. Вероятность вытащить 2 из первого И 2 из второго {probability} или {probability*100:0.2f}%")

# Вероятность вытащить 2 шара из первого ящика И 0 из второго
# ИЛИ 1 из первого И 1 из второго
# ИЛИ 0 из первого И 2 из второго
probability = combinations(7,2)*combinations(3,0)/combinations(10,2) * combinations(9,0)*combinations(2,2)/combinations(11,2) \
            + combinations(7,1)*combinations(3,1)/combinations(10,2) * combinations(9,1)*combinations(2,1)/combinations(11,2) \
            + combinations(7,0)*combinations(3,2)/combinations(10,2) * combinations(9,2)*combinations(2,0)/combinations(11,2)
print(f"2. Вероятность вытащить 2 белых из обоих ящиков {probability} или {probability*100:0.2f}%")

# Вероятность НЕ вытащить ни одного белого мяча необходимо вычесть из полной вероятности 1
probability = 1 - combinations(7,0)*combinations(3,2)/combinations(10,2) * combinations(9,0)*combinations(2,2)/combinations(11,2)
print(f"3. Вероятность вытащить хотябы (минимум) 1 белый {probability} или {probability*100:0.2f}%")