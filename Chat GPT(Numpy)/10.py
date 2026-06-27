import os
os.system('cls')

import numpy as np

np.random.seed(42) # supaya angka random selalu sama

data = np.random.randint(50, 100, size=(5, 4)) # buat random dari 50 - 100 | B = 5, K = 5

print("\nRaw Data")
print(data)

mean = np.mean(data, axis=0) # mean perkolom
std = np.std(data, axis=0)

print("\nMean per fitur: ")
print(mean)

print("\nStd per fitur: ")
print(std)

normalized = (data - mean) / std

print("\nNormalized data: ")
print(normalized)

threshold = 80
filtered = data[data[:, 0] >= threshold]

print("\nFiltered data (fitur pertama >= 80): ")
print(filtered)

weights = np.array([0.2, 0.3, 0.1, 0.4])
score = data @ weights

print("\nScore tiap data: ")
print(score)

best_index = np.argmax(score)

print("\nBest data index: ")
print(best_index)

print("\nBest data: ")
print(data[best_index])





