import os
os.system('cls')

import numpy as np

# array = np.array([10, 20, 30, 40, 50])

# print(array)
# view_array = array[1:4]
# view_array[0] = 999

# print("\nView: ")
# print(view_array)
# print(array)

# copy_array = array[1:4].copy()
# copy_array[0] = 777

# print("\nCopy: ")
# print(copy_array)
# print(array)

# print("Soal pertama")
# array = np.array([1, 2, 3, 4, 5])
# slice = array[1:4]
# print(slice)
# slice[0] = 100
# print(slice)

# print("\nSoal Kedua")
# array2 = np.array([10, 20, 30, 40, 50])
# slice2 = array2[1:4].copy()
# print(slice2)
# slice2[0] = 999
# print(slice2)

# print("\nSoal Ketiga")
# a = np.array([5, 10, 15, 20, 25])
# b = a[2:]
# b[1] = 999
# print(a)
# print(b)

# print(b.base)

# # keluarnya tetap 5, 10, 15, 20, 25, 
# # karena bukan print(b), 
# # index 3

# print("soal pertama")
# # outputnya 1,2,100,4,5. karena numpy berbeda dari python biasa jadi memori tetap lah memori
# print("soal kedua")
# a = np.array([10, 20, 30, 40, 50])
# b = a[1:4].copy() 
# b[1] = 999
# print(a)
# a = np.array([5, 10, 15, 20, 25])
# b = a[1:5]
# c = b[2:]
# c[0] = 999
# print(a)
# # 5, 10, 15, 999, 25| yang berubah index 3| b = 10,15, 20, 25. c = 20, 25


# kok bisa cuma tambah copy jadi gagal

print("\nSoal pertama")
array1 = np.array([5, 10, 15, 20, 25])
print(array1[0])
print(array1[2])
print(array1[4])

print("\nSoal Kedua")
array2 = np.array([10, 20, 30, 40, 50, 60])
print(array2[1:3])
print(array2[3:6])

print("\nSaol Ketiga")
array3 = np.array([[2, 4, 6],
                   [8, 10, 12],
                   [14, 16, 18]])
print(array3[1,2])
print(array3[0,:])
print(array3[:,1])

print("\nSoal Keempat")
array4 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]
                   ])
print(array4[1:3])
print(array4[:,2:4])
print('===')
print(array4[1: , 1:3])

print("\nSoal kelima")
array5 = np.array([100, 200, 300, 400, 500])
slice = array5[1:4]
slice[0] = 999
print(slice)
print(array5)
slice = array5[1:4].copy()
slice[0] = 777
print(slice)
print(array5)

