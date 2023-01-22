# Несмещенные стандартное отклонение и дисперсия
import numpy as np
x = np.array([167, 181, 174, 178, 175, 164, 182, 178, 193, 166, 154, 170, 177])
# СКО среднеквадратичное отклонине
print(f"standard deviation - стандартное отклонение {np.std(x, ddof=1)}")
# D(X) = npq = 𝞼^2
print(f"variance - дисперсия {np.var(x, ddof=1)}")
# 𝞼=√𝞼
print(f"корень квадратный из дисперсии {np.sqrt(np.var(x, ddof=1))}")