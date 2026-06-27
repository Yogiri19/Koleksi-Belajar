import os
os.system('cls')

import numpy as np
array = np.array([10, 20, 30, 40, 50])

print("\nArray 1D:" )
print(array)

print("\nIndexing")
print(array[0])
print(array[2])
print(array[-1])

print("\nSilencing ")
print(array[1:4]) # start:stop:step
print(array[:3])
print(array[2:])

array2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\nArray 2D")
print(array2d)

print("\nIndexing 2D: ")
print(array2d[0,0])
print(array2d[2,1])

print("\nSlicing 2D:")
print(array2d[0, :])
print(array2d[:, 1])
print(array2d[1:, 1:])

view_array = array[1:4]
view_array[0] = 999

print("\nView: ")
print(view_array)
print(array)

copy_array = array[1:4].copy()
copy_array[0] = 777

print("\nCopy: ")
print(copy_array)
print(array)