import os
os.system('cls')

import numpy as np
import time

# size = 1_000_000
# array = np.random.rand(size) 

# start = time.time()

# result_loop = []
# for x in array:
#     result_loop.append(x * 2)
# end = time.time()

# print(f"Ini array = ", array)
# print(f"Ini End = ", end)
# print(f"Ini start = ", start)
# print("Time: ", end - start)

# print("\nSoal Pertama")
# start = time.time()
# size = 500_000
# array = np.random.rand(size)

# LoopPython = []
# for i in array:
#     LoopPython.append(i * 3)
# end = time.time()
# print(end - start)

# print("\nSoal Kedua")
# start = time.time()
# LoopNumpy = array * 3
# end = time.time()
# print(end - start)

# print("\nSoal Ketiga")
# print(np.allclose(LoopPython, LoopNumpy))

# print("\nSoal Keempat")
# start1 = time.time()
# size1 = 200_000
# array1 = np.random.rand(size1)
# LoopPython1 = []
# for i in array1:
#     LoopPython1.append(i)

# end1 = time.time()
# print(f"Pake Python: {end - start}")
# start1 = time.time()
# LoopNumpy1 = array1
# end1 = time.time()
# print(f"pake Numpy: {end1 - start1}")

# print("\nSoal Kelima")
# start = time.perf_counter()
# size1 = 200_000
# array1 = np.random.rand(size1)
# for i in array1:
#     LoopPython1.append(i)
# end = time.perf_counter()
# print(f"Pake Python {end - start}")
# start = time.perf_counter()
# LoopNumpy1 = array1
# end = time.perf_counter()
# print(f"Ini pake Numpy{end - start}")

# print("\nSoal Keenam")
# array2 = np.multiply(array1, 2)
# print(array2)

# print("\nSoal Ketujuh")
# start = time.perf_counter()
# array1 = array1
# end = time.perf_counter()
# print(end-start)

# print("\nSoal Kedelapan")
print("\nSoal Pertama")
size1 = 100_000
array1 = np.random.rand(size1)
start1 = time.time()
looppython1 = []
for i in array1:
    looppython1.append(i * 5)
end1 = time.time()
print(end1 - start1)

start1 = time.time()
loopnumpy1 = array1 * 5
end1 = time.time()
print(end1 - start1)
print(np.allclose(looppython1, loopnumpy1))

print("\nSoal Kedua")
size2 = 300_000
array2 = np.random.rand(size2)
start2 = time.time()

looppython2 = [x * 2 for x in array2]
end2 = time.time()
print(end2 - start2)
start2 = time.time()
loopnumpy2 = array2 * 2
end2 = time.time()
print(end2 - start2)
print(np.allclose(looppython2, loopnumpy2))

print("\nSoal Ketiga")
size3 = 600_000
array3 = np.random.rand(size3)
start3 = time.time()
loopmulti1 = np.multiply(array3, 4)
end3 = time.time()
print(end3 - start3)

start3 = time.time()
loopnumpy3 = array3 * 4
end3 = time.time()
print(end3 - start3)
print(np.allclose(loopmulti1, loopnumpy3))

print("\nSoal Keempat")

size4 = 1_000_000
array4 = np.random.rand(size4)

start4 = time.time()
looppython4 = []
for i in array4:
    looppython4.append(i + 10)

end4 = time.time()
print(end4 - start4)

start4 = time.time()
loopnumpy4 = array4 + 10
end4 = time.time()
print(end4 - start4)
print(np.allclose(looppython4, loopnumpy4))

print("\nSoal Kelima")
size5 = 2_000_000
array5 = np.random.rand(size5)

start5 = time.perf_counter()
looppython5 = []
for i in array5:
    looppython5.append(i * 0.5)
end5 = time.perf_counter()
print(end5 - start5)

start5 = time.perf_counter()
loopnumpy5 = array5 * 0.5
end5 = time.perf_counter()
print(end5 - start5)

print(np.allclose(looppython5, loopnumpy5))