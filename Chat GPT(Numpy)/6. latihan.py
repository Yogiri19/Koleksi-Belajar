import os
os.system('cls')

import numpy as np

print("Soal Pertama")
array1 = np.array([5, 12, 18, 25, 40])
print(array1 > 15)
print(array1[array1 > 15])

print("\nSoal Kedua")
array2 = np.array([3, 6, 9, 12, 15])
print(array2 % 2 == 0)
print(array2[array2 % 2 == 0])

print("\nSoal Ketiga")
array3 = np.array([20, 35, 50, 65, 80])
print(array3[array3 >= 50])
print(array3 % 2 ==0)

print("\nSoal Keempat")
array4 = np.array([11, 22, 33, 44, 55])
print(array4[array4 < 40])
print(array4 / 11)

print("\nSoal kelima")
array5 = np.array([
    [70, 80, 90], # 80
    [40, 60, 75], # 58.3
    [85, 95, 65]  # 81.6
])
print(array5[array5 >= 80])
baris1 = np.mean(array5, axis=1)
print(array5[baris1 >= 80])

print("\nSoal keenam")
array6 = np.array([
    [70, 80, 90], # 80
    [40, 60, 75], # 58.3
    [85, 95, 65]  # 81.6
])
print(np.mean(array6, axis=1))
baris2 = np.mean(array6, axis=1)
print(array6[baris2 >= 75])

print("\nSoal ketujuh (Kolom)")
array7 = np.array([
    [50, 90, 70], # 65
    [85, 95, 80], # 86.6
    [60, 65, 75]  # 66.6
])
#    65| 83.3|75
kolom1 = np.mean(array7, axis=1)
print(array7[:,kolom1 >= 80])

print("\nSoal Kedelapan (baris)")
array8 = np.array([
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
])
baris3 = np.mean(array8, axis=0)
print(array8[baris3 >= 80])

print("\nSoal Kesembilan")
array9 = np.array([12, 25, 36, 49, 64, 81])
kuadrat = array9 % 2 != 0
print(array9[kuadrat])

baris4 = array9[array9 > 30 & array9 % 2 ==0]