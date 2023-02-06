import scipy.stats as stats
import numpy as np
gr1 =([0.5, 0.7, 1, 1.2, 1.4])
gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])
print(stats.kruskal(gr1, gr2, gr3))
h = 12 / n*(n+1) * (t1**2/len(gr1) + t2**2/len(gr2) + t3**2/len(gr3)) - 3 * (n+1)