import os
os.system('cls')

import numpy as np

array = np.array([10, 20, 30, 40, 50])
print(array)

print("\nStatistik 1D: ")
print(np.mean(array))
print(np.median(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.sum(array))

array2d = np.array([[10, 20, 30],
                    [40, 50, 60]])

print(array2d)
print("\nStatistik Keseluruhan: ")
print(np.mean(array2d))
print(np.sum(array2d))

print("\nAxis = 0 (per kolom): ")
print(np.mean(array2d, axis=0))
print(np.sum(array2d, axis= 0))
print("\n ini yang axisnya 1")
print(np.mean(array2d, axis=1))
print(np.sum(array2d, axis=1))

