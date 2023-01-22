# Медиана для четной и нечетной выборки
import numpy as np
def medianna(array):
    if len(array)%2:
        return array[len(array)//2]
    else: 
        return (array[len(array)//2-1]+array[len(array)//2])/2
         
z=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
print(len(z))
z.sort()
print(np.median(z))
print(medianna(z))
print(len(z)%2)
