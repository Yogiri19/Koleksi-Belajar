import os
os.system('cls')

import numpy as np

print("Soal Pertama")
array1 = np.array([1, 2, 3, 4, 5, 6])
print(array1.reshape(3,2))

print("\nSoal Kedua")
print(array1.T)

print("\nSoal Ketiga")
array3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(array3)
print(array3.flatten())
print(array3.ravel())

print("\nSoal Keempat")
array4 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array_flatten = array4.flatten()
array_flatten[0] = 999
print(array4)
print(array_flatten)
print("===")
array_ravel = array4.ravel()
array_ravel[0] = 777
print(array4)
print(array_ravel)

print("\nSoal kelima")
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
print(np.stack((a,b)))
print(np.hstack((a,b)))
print(np.vstack((a,b)))

print("\nSoal keenam")
array6 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array6.reshape(4,2))

print("\nSoal Ketujuh")
array7 = np.array([1, 2, 3, 4, 5, 6])
#print(np.hstack(np.vstack(array7)))
print(np.hstack((array7, array7)))
print(np.vstack((array7, array7)))

print("\nSoal Kedelapan")
array8 = np.array([
    [1, 2],
    [3, 4]
])
flatten0 = array8.flatten()
flatten0[0] = 99
print(array8)
print(flatten0)
print("===")
ravel0 = array8.ravel()
ravel0[0] = 777
print(array8)
print(ravel0)

print("\nSoal Kesembilan")
array9 = np.array([1, 2, 3, 4, 5, 6])
reshape1 = array9.reshape(2,3)
t1 = reshape1.T
flatten1 = t1.flatten()
print(flatten1)

print("\nSoal kesepuluh")
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.hstack(np.stack(a,b)))
