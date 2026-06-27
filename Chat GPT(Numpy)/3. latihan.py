import os
os.system('cls')

import numpy as np

# print("\nSoal Pertama")
# array = np.array([2, 4, 6, 8, 10])
# print(array + 5)
# print(array - 1)
# print(array * 2)
# print(array / 4)

# print("\nSoal Kedua")
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
# print(a + b)
# print(b - a)
# print(a * b)

# print("\nSoal Ketiga")
# 6, 12, 18. 6, 12, 18. 1, 2, 3. karena array itu dikali, ditambah, dan dibagi
# print("Soal Keempat")
# eror, karena list nya kurang 1, solusinya tambah 1 list 30, maka hasilnya 11, 22, 33

# print("\nSoal kelima")
# karena lebih singkat cepat dan efisien

# print("/nSoal Pertama")
# array1 = np.array([5, 10, 15, 20, 25])
# print(array1[0])
# print(array1[4])
# print(array1[1:4])

# print("\nSoal Kedua")
# array2 = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# print(array2[1,1])
# print(array2[1,:])
# print(array2[:,2])
# print(np.sum(array2))

# print("\nSoal Ketiga")
# array3 = np.array([10, 20, 30, 40, 50])
# slice = array3[1:4]
# slice[0] = 999
# print(slice)
# print(array3)
# slice = array3[1:4].copy()
# slice[0] = 777
# print(slice)
# print(array3)

# print("soal pertama")
# array1 = np.array([1, 4, 9, 16, 25])
# print(np.sqrt(array1))
# print(np.power(array1, 2))

# print("\nsoal kedua")
# array2 = np.array([1, 2, 3])
# print(np.exp(array2))
# print(np.log(array2))
# print(np.log(np.exp(array2)))

# print("\nsoal ketiga")
# array3 = np.array([2, 4, 6])
# pangkat = np.power(array3, 3)
# kuadrat = np.sqrt(pangkat)
# log = np.log(kuadrat)
# print(array3)
# print(pangkat)
# print(kuadrat)
# print(log)

# print("\nsoal pertama")
# array1 = np.array([[1, 2, 3],
#                    [4, 5, 6]])
# print(array1 + 5)

# print("\nSoal Kedua")
# array2 = np.array([[10, 20, 30],
#                    [40, 50, 60]])
# vector = np.array([1, 2, 3,])
# print(vector + array2)

# print("\nSoal Ketiga")
# array3 = np.array([[1, 2, 3],
#                    [4, 5, 6]])
# vector = np.array([10, 20])
# vector = vector.reshape(-1, 1) # apa itu reshape
# print(array3 + vector)

print("soal pertama")
array1 = np.array([2, 4, 6, 8])
print(array1 + 5)
print(array1 * 2)

print("\nsoal kedua")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * b)

print("\nsoal ketiga")
array3 = np.array([1, 9, 16, 25])
print(np.sqrt(array3))
print(np.power(array3, 2))

print("\nsoal Keempat")
array4 = np.array([1, 2, 3])
print(np.exp(array4))
print(np.log(np.exp(array4)))

print("\n Soal kelima")
array5 = np.array([2, 4, 6])
print(array5 * 3)
print(np.sqrt(array5 * 3))

print("\n Soal keenam")
array5 = np.array([[1, 2],
                   [3, 4]])
print(array5 + 10)

print("\n Soal Ketujuh")
array6 = np.array([[1, 2, 3],
                   [4, 5, 6]])
vector = np.array([10, 20, 30])
print(array6 + vector)

print("\nSoal Kedelapan")
array2d = np.array([[1, 2, 3],
                    [4, 5, 6]])
vector = np.array([100, 200])
vector = vector.reshape(-1, 1)
print(array2d + vector)

print("\nSoal Kesembilan")
array9 = np.array([1, 2, 3])
a = np.exp(array9)
b = a + 1
print(a)
print(b)
print(np.log(b))

# print("\nSoal Sepuluh")
# output nya 11, 24, 36, karena array * 2 == 1, 4, 6 dan ditambah vector