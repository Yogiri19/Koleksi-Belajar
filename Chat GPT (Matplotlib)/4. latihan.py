import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5, 6]
# y = [2, 4, 5, 7, 10, 12]
# colors = [10, 20, 30, 40, 50, 60]
# plt.figure()
# plt.scatter(x,y,
#             c=colors)
# plt.title("Coba Coba")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar(label="ini color")
# plt.show()

# x_rand = np.random.rand(50)
# y_rand = np.random.randint(50)
# print(x_rand)

# print(y_rand)

# Soal Pertama
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.scatter(x,y)
plt.title("Soal Pertama")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Soal Kedua
x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]
plt.figure()
plt.scatter(x,y,
            color=["red"])
plt.show()

# Soal Ketiga
x = [2, 4, 6, 8, 10]
y = [3, 6, 7, 9, 12]
plt.figure()
plt.scatter(x,y,
            s=120)
plt.show()

# Soal Keempat
x = [1, 3, 5, 7, 9]
y = [9, 7, 5, 3, 1]
colors = [5, 15, 25, 35, 45]
plt.figure()
plt.scatter(x,y,
            c=colors)
plt.colorbar()
plt.show()

# Soal Kelima
x = np.random.rand(30)
y = np.random.rand(30)
plt.figure()
plt.scatter(x,y)
plt.show()

# Soal Keenam
x = [5, 10, 15, 20, 25]
y = [8, 16, 20, 26, 30]
plt.figure()
plt.scatter(x,y,
            alpha=0.6)
plt.show()

# Soal Ketujuh
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 6, 7, 9]
sizes = [40, 80, 120, 160, 200, 240]
plt.figure()
plt.scatter(x,y,
            s=sizes)
plt.show()

# Soal Kedelapan
x = np.random.randint(0, 100, 60)
y = np.random.randint(0, 100, 60)
plt.figure()
plt.scatter(x,y)
plt.show()

# Soal Kesembilan
x = [10, 20, 30, 40, 50]
y = [5, 15, 25, 35, 45]
colors = [100, 80, 60, 40, 20]
plt.figure()
plt.scatter(x,y,
            c=colors)
plt.colorbar()
plt.show()

# Soal Kesepuluh
x =  [2, 4, 6, 8, 10]
y = [1, 3, 6, 7, 9]
colors = [10, 20, 30, 40, 50]
plt.figure()
plt.scatter(x,y,
            c=colors,
            s=150,
            alpha=0.7)
plt.title("Soal Kesepuluh")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()