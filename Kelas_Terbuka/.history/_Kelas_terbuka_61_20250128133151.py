import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a}")
#print(f"a pangkat 2 {list_a**2}") <- ini akan gagal
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b**2 = \n{matrix_b**2}")

# membuat matrix kosong
zeros_c = np.zeros((2,2))
print(f"zeros_c = \n{zeros_c}")