import scipy.stats as stats
import numpy as np
x = np.array([1000, 1380, 1200])
y = np.array([1400,  1600,  1180,  1220])
print(stats.mannwhitneyu(x, y))

X = np.array([20,17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
Y = np.array ([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])
print(stats.wilcoxon(X, Y))

X2 = np.array([ 32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
Y2 = np.array ([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])
stats.wilcoxon(X2, Y2)

gr1 =([0.5, 0.7, 1, 1.2, 1.4])
gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])
print(stats.kruskal(gr1, gr2, gr3))