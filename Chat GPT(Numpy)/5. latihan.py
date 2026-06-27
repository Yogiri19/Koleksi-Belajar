import os
os.system('cls')

import numpy as np

# array = np.array([10, 20, 30, 40, 50])

# print(np.mean(array))
# print(np.std(array))
# print(np.median(array))
# print(np.max(array))
# print(np.min(array))
# print(np.var(array))
# print(np.sum(array))


# print("\narray 2d")
# array2d = np.array([[10, 20, 30],
#                     [40, 50, 60]])
# print(np.mean(array2d))
# print(np.std(array2d))
# print(np.median(array2d))
# print(np.max(array2d))
# print(np.min(array2d))
# print(np.var(array2d))
# print(np.sum(array2d))
print("Soal pertama")
array1 = np.array([5, 10, 15, 20, 25])
print(np.mean(array1))
print(np.sum(array1))

print("\nSoal kedua ")
array2 = np.array([2, 4, 6, 8])
print(np.min(array2))
print(np.max(array2))

print("\nSoal ketiga ")
array3 = np.array([10, 20, 30, 40])
print(np.var(array3))
print(np.median(array3))

print("\nSoal Keempat")
array4 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(np.mean(array4))
print(np.sum(array4))

print("\nSoal kelima")
array5 = np.array([[10, 20, 30],
                   [40, 50, 60]])
print(np.max(array5))
print(np.min(array5))

print("\nSoal keenam")
array6 = np.array([[2, 4, 6],    # b = 4
                   [8, 10, 12]]) # b = 10
print(np.mean(array6, axis=1))
print(np.mean(array6, axis=0))


print("\nSoal ketujuh")
array7 = np.array([[1, 3, 5],
                   [7, 9, 11]])
print(np.std(array7))
print(np.var(array7))

print("\nSoal kedelapan")
array8 = np.array([3, 6, 9, 12, 15])
print(np.mean(array8))
print(np.std(array8))
print(np.var(array8))

print("\nSoal kesembilan")
array9 = np.array([[5, 10, 15],
                   [20, 25, 30]])
print(np.sum(array9, axis=0))
print(np.max(array9, axis=1))


print("\nSoal kesepuluh")
mean = 5
sum = 20
var = 200