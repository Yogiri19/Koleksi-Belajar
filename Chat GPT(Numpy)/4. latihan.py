import os
os.system('cls')

import numpy as np

# print("zeros")
# array_zeros = np.zeros(5)
# array2d = np.zeros((2,99))
# print(array_zeros)
# print(array2d)

# print("\nones")
# array_ones = np.ones(5)
# array2d = np.ones((3,2))
# print(array_ones)
# print(array2d)

# print("\neye")
# array_eye = np.eye(4)
# print(array_eye)

# print("\nsoal pertama")
# array = np.zeros(5)
# print(array)

# print("\nsoal kedua")
# array = np.ones(4)
# print(array)

# print("\nsoal ketiga")
# array = np.zeros((2,3))
# print(array)

# print("\nsoal keempat")
# array = np.ones((3,2))
# print(array)

# print("\nsoal kelima")
# array = np.eye(4)
# print(array)

# print("\nsoal keenam")
# array = np.eye(3)
# array = array * 5
# print(array)

# print("\nsoal ketujuh")
# print(np.ones((2,3))*2)
# array = np.ones((2,3)) * 2 + np.zeros((2,3)) # bisa ditambah ternyata
print("random float; 0-1")
array1 = np.random.rand(5) # menghasilkan 5 element
array12 = np.random.rand(5,3)
array13 = np.random.rand(5) * 10 + 5 # agar melewati batas
print(array1)
print(array12)
print(array13)

print("\nRandom normal distribution: ")
array2 = np.random.randn(7) # 7 element
print(array2)

print("\nRandom integer: ")
array3 = np.random.randint(1, 100, size=9) # element nya 9
print(array3)

print("\nRandom reproducible")
np.random.seed(8) # seed ini agar pasti dan memilih secara acak
array4 = np.random.rand(5)
print(array4)