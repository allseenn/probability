# Расчет квартилей
import numpy as np
z=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#z=np.array([1, 2, 4, 2, 1, 5, 7, 2, 3, 5, 7, 8, 9])
z.sort()
# Если n*k/100 целое число, то k-ая перцентиль - это среднее значение элементов n*k/100 и n*k/100+1
# Если n*k/100 не целое число, то k-ая перцентиль это полученное число окрегленное в большую сторону
def percentile(array, percent):
    if len(array)*percent/100%2:
        digit=len(array)*percent/100
        print(f"if {digit}")
        return array[int(digit)]
    else:
        digit1=len(array)*percent/100-1
        digit2=len(array)*percent/100
        print(f"else {digit1} {digit2}")
        return (array[int(digit1)]+array[int(digit2)])/2
print(percentile(z, 5))
print(np.percentile(z, 5))
