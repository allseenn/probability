# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def bernulli(n,p,k):
    return combinations(n,k)*p**k*(1-p)**(n-k)

n = 100
k = 85
p = 0.8

print(f"Вероятность попасть 85 раз при 100 выстрелах {bernulli(n,p,k)} или {bernulli(n,p,k)*100:1.2f}%")
