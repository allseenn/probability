# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def bernulli(n,p,k):
    return combinations(n,k)*p**k*(1-p)**(n-k)

n = 144
k = 70
p = 1/2

print(f"Вероятность, что орел выпадет ровно 70 раз из 144 составляет {bernulli(n,p,k)} или {bernulli(n,p,k)*100:2.2f}%")