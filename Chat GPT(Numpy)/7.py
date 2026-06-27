import os
os.system('cls')

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

print(array)

print("\nreshape:") # Mengubah bentuk menjadi 2 D
array2d = array.reshape(2,3)
print(array2d)

print("\nTranspose: ")
print(array2d.T) # tukar baris ke kolom

print("\nFlatten: ")
flatten_array = array2d.flatten()
print(flatten_array)

print("\nRavel: ")
ravel_array = array2d.ravel()
print(ravel_array)

print("\nSetelah ubah flatten: ") # ini copy
flatten_array[0] = 999
print(flatten_array)
print(array2d)

print("\nSetelah diubah ke ravel: ") # ini view
ravel_array[0] = 777
print(ravel_array)
print(array2d)

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print("\nStack")
print(np.stack((array_a, array_b)))

print("\nHorizontal Stack: ")
print(np.hstack((array_a, array_b)))

print("\nVertikal Stack:")
print(np.vstack((array_a, array_b)))