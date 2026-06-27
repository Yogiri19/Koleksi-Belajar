import os
os.system('cls')

import numpy as np

print("\nSoal Pertama")
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
print(np.dot(a,b))

print("\nSoal Kedua")
array2 = np.array([
    [3, 1],
    [5, 2]
])
print(array2.T)

print("\nSoal ketiga")
array3 = np.array([
    [4, 7],
    [2, 6]
])
print(np.linalg.det(array3))

print("\nSoal Keempat")
a2 = np.array([
    [1, 0],
    [2, 1]
])
b2 = np.array([
    [3, 4],
    [5, 6]
])
print(np.dot(a2, b2))

print("\nSoal Kelima")
array5 = np.array([
    [2, 1],
    [5, 3]
])
print(np.linalg.inv(array5))

print("\nSoal Keenam")

array6 = np.array([
    [1, 2],
    [3, 4]
])
inv1 = np.linalg.inv(array6)
print(array6 @ inv1)

print("\nSoal Ketujuh")
array7 = np.array([
    [1, 2],
    [2, 1]
])
eig1 = np.linalg.eig(array7)
print(eig1)

print("\nSoal Kedelapan")
array8 = np.array([
    [1, 2],
    [2, 1]
])
eig2 = np.linalg.eig(array8)
print(eig2)
print(np.linalg. eig(eig2))


print("\nSoal Kesembilan")
array9 = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.det(array9))
inv2 = np.linalg.inv(array9)
print(inv2)
print(array9 @ inv2)

print("\nSoal Sepuluh")
a3 = np.array([1, 2, 3, 4])
b3 = np.array([4, 3, 2, 1])

print(np.dot(a3, b3))