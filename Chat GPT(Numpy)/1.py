#==========CATATAN
# [baris, kolom] = baris dulu baru kolom
# : -> semua, (kiri = baris)| (kalo kanan = kolom)
# kiri baris, kanan kolom
import os
os.system("cls")

import numpy as np
#== ndarray = N-dimensional array


# print("\nArray 1D:")
# print(array)

# print("dtype :", array.dtype)
# print("shape :", array.shape) # karena 5 kolom
# print("ndim  :", array.ndim)
# print("size  :", array.size)

# array2d = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print("\nArray 2D:")
# print(array2d)

# print("dtype :", array2d.dtype)
# print("shape :", array2d.shape)
# print("ndim  :", array2d.ndim)
# print("size  :", array2d.size)

# array_float = np.array([1, 2, 3], dtype=float)

# print("\nArray float:")
# print(array_float)
# print("dtype :", array_float.dtype)

#=== list python
list_python = [1, 2, 3]
array_numpy = np.array([1, 2, 3])

print("\nList Python:")
print(list_python)
print("List + List:")
print(list_python + list_python)
print("\nNumPy Array:")
print(array_numpy)
print("Array + Array:")
print(array_numpy + array_numpy)

