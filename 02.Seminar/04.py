# Подбрасывают 4 одинаковые монеты. Какова вероятность, что решка выпадет 
# не более 1 раза
# P(X=K) = Cnk*p**k*q**(n-k), где q = 1-p
# P(X<=1) = P(X=0) + P(X=1)
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def bernulli(n,p,k):
    return combinations(n,k)*p**k*(1-p)**(n-k)

n = 4
p = 1/2
k0 = 0
k1 = 1

print(f"Вероятность решки выпасть не более 1 раза при 4 подбросах {(bernulli(n,p,k0) + bernulli(n,p,k1))*100:2.2f}%")