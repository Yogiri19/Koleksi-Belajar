import os
os.system('cls')

import numpy as np

print("Zero:")
array = np.zeros(5)
print(array)

print("\nnones: ")
array = np.ones(5)
print(array)

print("\neye:")
array = np.eye(4)
print(array)

print("\narange")
array = np.arange(0, 10, 2)
print(array)

print("\nlinspace: ")
array = np.linspace(0, 1, 5)
print(array)

print("\nrandom float 0-1: ")
array = np.random.rand(5)
print(array)

print("\nRandom normal distribution: ")
array = np.random.randn(5)
print(array)

print("\nRandom Integer: ")
array = np.random.randint(1, 100, size=5)
print(array)

print("\nRandom reproducible:")
np.random.seed(42)
array = np.random.rand(5)
print(array)