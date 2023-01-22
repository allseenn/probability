# Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки
def arithmetic_mean(array):
    return sum(array)/len(array)

def variance(array, d=0):
    x = arithmetic_mean(array)
    summa = 0
    for i in array:
        summa += (i - x)**2
    return summa/(len(array)-d)

data = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
data.sort()
print(f"Среднее арифметическое {arithmetic_mean(data)}")
print(f"Смещенное СКО {variance(data)**0.5}")
print(f"Несмещенное СКО {variance(data, 1)**0.5}")
print(f"Смещенная дисперсия {variance(data)}")
print(f"Несмещенная дисперсия {variance(data, 1)}")