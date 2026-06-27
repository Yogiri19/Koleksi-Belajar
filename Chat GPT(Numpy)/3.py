import os
os.system('cls')

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Array: ")
print(array)
print("\nOperasi dasar: ")
print(array + 10)
print(array - 2)
print(array * 3)
print(array / 2)

array2 = np.array([10, 20, 30, 40, 50])
print(array + array2)
print(array * array2)

print("\nFungsi Matematika: ")
array = np.array([1, 2, 3, 4, 5])
print(np.sqrt(array))   # ini dukuadratin per masing masing list
print(np.power(array,2))# ini dipangkatin 
print(np.exp(array))    # ini membesarkan nilai cepat
print(np.log(array))    # menormalkan

array2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nArray 2D: ")
print(array2d)

print("\nBroadcasting: ")
print(array2d + 10)

vector = np.array([10, 20, 30])
print("\nBroadcasting dengan vector: ")
print(array2d + vector)
