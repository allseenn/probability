# Найти вероятность, что среди взятых наугад 5 деталей 2 стандартные, если 
# вероятность детали быть стандартной равна 0.9
import math
def combinations(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def bernulli(n,p,k):
    return combinations(n,k)*p**k*(1-p)**(n-k)

p = 0.9
n = 5
k = 2

print(f"Вероятность взять 2 стандартных детали равно {bernulli(n,p,k)*100:1.2}%")