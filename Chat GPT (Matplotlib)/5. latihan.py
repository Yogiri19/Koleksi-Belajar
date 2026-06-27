import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np

# # Soal Pertama
# x = [1, 2, 3, 4]
# y1 = [2, 3, 5, 7]
# y2 = [1, 4, 6, 8]

# plt.figure()
# plt.subplot(1,2,1)
# plt.plot(x,y1)
# plt.title("Grafik A")

# plt.subplot(1, 2, 2)
# plt.plot(x,y2)
# plt.title("Grafik A")
# plt.show()

# # Soal Kedua
# x = [1, 2, 3, 4, 5]
# y1 = [3, 6, 9, 12, 15]
# y2 = [5, 7, 9, 11, 13]

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x,y1)
# plt.title("Atas")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2)
# plt.title("Bawah")
# plt.show()

# # Soal Ketiga
# x = [0, 1, 2, 3]
# y1 = [1, 4, 9, 16]
# y2 = [16, 9, 4, 1]

# plt.figure()
# plt.subplot(1, 2, 1)
# plt.plot(x,y1)
# plt.title("Naik")

# plt.subplot(1, 2, 2)
# plt.plot(x,y2)
# plt.title("Turun")
# plt.show()

# # Soal Keempat
# x = [1, 2, 3, 4, 5]
# y1 = [2, 5, 7, 10, 13]
# y2 = [3, 6, 8, 11, 14]
# y3 = [5, 8, 6, 9 , 12]

# plt.figure()
# plt.subplot(2, 2, 1)
# plt.plot(x,y1)
# plt.title("A")

# plt.subplot(2, 2, 2)
# plt.plot(x,y2)
# plt.title("B")

# plt.subplot(2, 2, 3)
# plt.plot(x,y3)
# plt.title("C")

# plt.subplot(2, 2, 4)
# plt.plot(x,y1)
# plt.title("D")
# plt.show()

# # Soal Kelima
# x = [1, 2, 3, 4]
# y1 = [4, 8, 12, 16]
# y2 = [2, 3, 5, 7]

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x,y1)
# plt.title("pertama")
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2)
# plt.title("Kedua")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Soal Keenam
# x = [0, 1, 2, 3, 4]
# y1 =[1, 2, 4, 8, 16]
# y2 = [16, 8, 4, 2, 1]

# plt.figure()
# plt.subplot(1, 2, 1)
# plt.plot(x,y1)
# plt.title("Pertama")

# plt.subplot(1,2,2)
# plt.plot(x,y2)
# plt.title("Kedua")
# plt.show()

# # Soal Ketujuh
# x = [1, 2, 3, 4, 5]
# y1 = [3, 5, 7, 9, 11]
# y2 = [2, 4, 8, 16, 32]
# y3 = [10, 9, 8, 7, 6]

# plt.figure()
# plt.subplot(2,2,1)
# plt.plot(x,y1)

# plt.subplot(2,2,2)
# plt.plot(x,y2)

# plt.subplot(2,2,3)
# plt.plot(x,y3)

# plt.subplot(2,2,4)
# plt.show()

# # Soal Kedelapan
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 8, 16, 32]
# y2 = [32, 16, 8, 4, 2]
# y3 = [5, 10, 15, 20, 25]
# y4 = [1, 4, 9, 16, 25]

# fig,axs = plt.subplots(2,2)

# axs[0,0].plot(x,y1)
# axs[0,1].plot(x,y2)
# axs[1,0].plot(x,y3)
# axs[1,1].plot(x,y4)
# plt.show()

# # Soal Kesembilan
# x = [1, 2, 3, 4]
# y1 = [10, 20, 30, 40]
# y2 = [40, 30, 20, 10]

# plt.figure()
# plt.subplot(1,2,1)
# plt.plot(x,y1)
# plt.suptitle("Judul figure besar")

# plt.subplot(1, 2, 2)
# plt.plot(x,y2)
# plt.show()

# # Soal Kesepuluh
# x = [1, 2, 3, 4, 5]
# y1 = [5, 10, 15, 20, 25]
# y2 = [25, 20, 15, 10, 5]
# y3 = [2, 4, 6, 8, 10]

# fig,axs = plt.subplots(2,2)

# axs[0,0].plot(x,y1)

# axs[0,1].plot(x,y2)

# axs[1,0].plot(x,y3)
# plt.show()

# Soal Pertama
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

fig,axs = plt.subplots(1,2)
axs[0].plot(x,y1)
axs[0].set_title("Linear Genap")

axs[1].plot(x,y2)
axs[1].set_title("Linear Ganjil")
plt.show()

# Soal Kedua
x = [0, 1, 2, 3, 4]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]
y3 = [2, 4, 6, 8, 10]

fig,axs= plt.subplots(2,2)
axs[0,0].plot(x,y1)
axs[0,0].set_title("pertama")

axs[0,1].plot(x,y2)
axs[0,1].set_title("Kedua")
axs[1,0].plot(x,y3)
axs[1,0].set_title("Ketoga")

plt.show()

# Soal Ketiga
x = [1, 2, 3, 4, 5]
y1 = [5, 10, 15, 20, 25]
y2 = [25, 20, 15, 10, 5]
y3 = [3, 6, 9, 12, 15]
y4 = [1, 8, 27, 64, 125]

fig,axs = plt.subplots(2,2)
axs[0,0].plot(x,y1)
axs[0,0].set_title("Pertama")

axs[0,1].plot(x,y2)
axs[0,1].set_title("Kedua")

axs[1,0].plot(x,y3)
axs[1,0].set_title("Ketiga")

axs[1,1].plot(x,y4)
axs[1,1].set_title("Keempat")
fig.suptitle("Moderen Subplot Layout")

plt.show()