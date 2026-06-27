import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np

# DATA DASAR
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 7, 10, 12]

# SCATTER PLOT DASAR
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot Dasar")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# SCATTER DENGAN WARNA
plt.scatter(x, y,
            color="red")
plt.title("scatter dengan warna")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# SCATTER DENGAN TITIK 
plt.figure()
plt.scatter(x, y,
            s=100) # s = size
plt.title("Scatter Dengan Ukuran Titik")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# SCATTER DENGAN WARNA BERDASARKAN NILAI
colors = [10, 20, 30, 40, 50, 60]
plt.figure()
plt.scatter(x,y,
            c=colors) 
plt.title("Scatter Dengan Color Mapping")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="Nilai Warna")
plt.show()

# SCATTER DATA ACAK
x_rand = np.random.rand(50) # 50 angka acak dari 0-1
y_rand = np.random.rand(50)

plt.figure()
plt.scatter(x_rand, y_rand)
plt.title("Scatter Data Acak")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
