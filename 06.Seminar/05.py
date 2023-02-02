# Найдите 95% доверительные интервалы для долей больных, 
# которые не чувствовали боли при включенном и выключенном приборе.
# Можно ли по этим интервалам оценить статистическую значимость различий?
import numpy
n = 30
p = 24/30
print(p+1.96*numpy.sqrt((p*(1-p))/n))
print(p-1.96*numpy.sqrt((p*(1-p))/n))