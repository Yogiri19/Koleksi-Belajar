import os
os.system('cls')

import numpy as np
array = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("\nVector: ")
print(array)
print(array2)

print("\nDot Product: ")
print(np.dot(array,array2)) # Penjumhalah Kolom

matrix1 = np.array([
    [1, 2], # baris dulu
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix: ")
print(matrix1)
print(matrix2)

print("\nMatrix Multiplication: ")
print(np.dot(matrix1, matrix2))
print(matrix1 @ matrix2) # aturannya baris A x kolom b

print("\nTranspose: ") # menukar baris menjadi kolom
print(matrix1.T)

print("\nDeterminant: ")
print(np.linalg.det(matrix1)) # ad - bc = 1*4 - 2*3 = -2 | linear algebra

print("\nInverse Matrix:")
inverse_matrix = np.linalg.inv(matrix1)
print(inverse_matrix)

print("\nCheck Identity: ")
print(matrix1 @ inverse_matrix)

print("\nEigen value & vector:")
eigen_value, eigen_vector = np.linalg.eig(matrix1)
print(eigen_value)
print(eigen_vector)
