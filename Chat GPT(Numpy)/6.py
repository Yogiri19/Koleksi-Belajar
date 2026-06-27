import os
os.system('cls')

import numpy as np

array = np.array([10, 25, 30, 45, 60, 75])
print(array)

print("\nKondisi Boolean")
print(array > 30)
print(array % 2 == 0)

print("\nFiltering data:")
print(array[array > 30]) # agar tidak bool
print(array[array % 2 == 0]) # agar tidak bool

print("\nArray 2d")
array2d = np.array([
    [65, 70, 80],
    [90, 55, 60],
    [75, 85, 95]
])
print(array2d)

print("\nFiltering nilai >= 80:")
print(array2d[array2d >= 80])

print("\nFiltering per baris (mean >=80):")
mean_per_row = np.mean(array2d, axis=1)
print(mean_per_row) #(65+70+80)/3 = 71.6
                    #(90+55+60)/3 = 68.3
                    #(75+85+95)/3 = 85 

print(array2d[mean_per_row >= 80]) # ambil baris yang meannya >= 80
                                   # karena baris 3 itu 85