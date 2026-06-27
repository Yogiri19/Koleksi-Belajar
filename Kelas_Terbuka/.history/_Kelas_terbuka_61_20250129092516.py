import numpy as np
import os
os.system("cls")
# list_a = [1,2,3,4]
# vector_a = np.array([1,2,3,4])

# print(f"list_a = {list_a}")
# #print(f"a pangkat 2 {list_a**2}") <- ini akan gagal
# print(f"vector_a = {vector_a}")
# print(f"a pangkat 2 = {vector_a**2}")
# print(f"a kali 5 = {vector_a*5}")
# print("===pangkat==")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = {matrix_b}")
print(f"matrix b**2 = {matrix_b**2}")
print("===array==")

print("===zeros=")
# membuat matrix kosong
zeros_c = np.zeros((2,2))
print(f"zeros_c = {zeros_c}")
ones_d = np.ones((2,2))
print(f"ones_d = {ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah =  {jumlah}")

