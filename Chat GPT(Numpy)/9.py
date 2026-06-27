import os
os.system('cls')

import numpy as np
import time

size = 1_000_000 # "_" hanya untuk mudah dibaca

array = np.random.rand(size) # angka acak 0-1 dan jumlah datanya 1 juta

# cara lambat python
start = time.time()# Jumlah detik sejak 1 jan 1970
result_loop = []
for x in array: # menjadikan loop python
    result_loop.append(x * 2)
end = time.time()

print("\nLoop Python")
print("Time: ", end - start)

start = time.time()
result_numpy = array * 2
end = time.time()

print("\nVectorized Numpy: ")
print("Time", end - start)

print("\nCheck equal: ")
print(np.allclose(result_loop, result_numpy))