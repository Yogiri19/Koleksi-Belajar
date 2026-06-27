import os
os.system("cls")

import matplotlib.pyplot as plt

# # Soal Pertama
# x = [1, 2, 3, 4 , 5]
# y1 = [2, 4, 6, 8, 10]

# plt.figure(figsize=(8,4))
# plt.plot(x,y1)
# plt.title("latihan 1")
# plt.xlabel("X")
# plt.ylabel("Y1")
# plt.show()

# # Soal Kedua
# x = [0, 1, 2, 3, 4]
# y1 = [1, 1, 2, 3, 5]

# plt.figure(figsize=(12,6))
# plt.plot(x,y1)
# plt.title("Figure Besar")
# plt.show()

# # Soal Ketiga
# x = [1, 2, 3, 4, 5]
# y1 = [5, 4, 3, 2, 1]

# plt.figure(figsize=(6,4), dpi=150)
# plt.plot(x,y1)
# plt.title("DPI 150")
# plt.show()

# # Soal keempat
# x = [1, 2, 3, 4]
# y1 = [1, 4, 9, 16]
# y2 = [2, 3, 5, 7]

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x,y1)
# plt.title("Kuadrat")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2)
# plt.title("Prima")
# plt.show()

# # Soal Kelima
# x = [1, 2, 3, 4, 5]
# y1 = [3, 1, 4, 1, 5]
# y2 = [1, 2, 3, 4, 5]

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x,y1)
# plt.title("Pertama")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2)
# plt.title("Kedua")

# plt.tight_layout()
# plt.show()

# # Soal Keenam
# x = [1, 2, 3, 4, 5]
# y1 = [10, 20, 15, 25, 30]
# y2 = [30, 25, 20, 15, 10]

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x,y1)

# plt.subplot(2, 1, 2)
# plt.plot(x,y2)

# plt.subplots_adjust(hspace=0.6)
# plt.show()

# # Soal Ketujuh
# x = [0, 2, 4, 6, 8]
# y1 = [0, 1, 0, 1, 0]
# y2 = [1, 0, 1, 0, 1]

# plt.figure(figsize=(9,5))
# plt.subplot(2, 1, 1)
# plt.plot(x,y1,
#          color="blue")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2,
#          color="red")
# plt.show()

# # Soal Kedelapan
# x = [1, 2, 3, 4, 5]
# y1 = [1, 8, 27, 64, 125]
# y2 = [1, 4, 9, 16, 25]
# y3 = [2, 4, 8, 16, 32]

# plt.figure(figsize=(8,10))
# plt.subplot(3, 1, 1)
# plt.plot(x,y1)
# plt.xlabel("X")
# plt.ylabel("Y1")

# plt.subplot(3, 1, 2)
# plt.plot(x,y2)
# plt.xlabel("X")
# plt.ylabel("Y2")

# plt.subplot(3, 1, 3)
# plt.plot(x,y3)
# plt.xlabel("X")
# plt.ylabel("Y3")

# plt.tight_layout()
# plt.show()

# # Soal Kesembilan
# x = [1, 2, 3, 4, 5, 6]
# y1 = [2, 3, 5, 7, 11, 13]
# y2 = [1, 1, 2, 3, 5, 8]

# plt.figure(figsize=(10,6), dpi=120)

# plt.subplot(2, 1, 1,)
# plt.subplots_adjust(hspace=0.4)
# plt.plot(x,y1)
# plt.title("Prima")

# plt.subplot(2, 1, 2)
# plt.subplots_adjust(hspace=0.6)
# plt.plot(x,y2,)
# plt.title("Fibonacci")

# plt.show()

# # Soal Kesepuluh
# x = [1, 2, 3 , 4, 5]
# y1 = [5, 10, 15, 20, 25]
# y2 = [25, 20, 15, 10, 5]

# plt.figure(figsize=(8,6))
# plt.subplot(2, 1, 1)
# plt.plot(x,y1,
#          marker="o")

# plt.subplot(2, 1, 2)
# plt.plot(x,y2,
#          marker="s")
# plt.tight_layout()
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# Soal Pertama
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x,y1)
plt.show()

# Soal Kedua
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

plt.figure()
plt.scatter(x,y1)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Soal Ketiga
x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 15, 25]

plt.figure()
plt.bar(x,y1)
plt.show()

#Soal Keempat
y1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]

plt.figure()
plt.hist(y1,
         bins=5)
plt.show()

# Soal Kelima
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2  = [0, 1, 2, 3, 4]

plt.figure()

plt.plot(x,y1,
         label="Kuadratik")
plt.plot(x,y2,
         label="Linear")
plt.legend()
plt.show()

# Soal Keenam
x = [1, 2, 3, 4]
y1 = [1, 3, 2, 4]
y2 = [2, 4, 1, 3]

plt.figure()
plt.subplot(2, 1, 1)
plt.scatter(x,y1)
plt.title("atas scatter plot y1 vs x")

plt.subplot(2, 1, 2)
plt.plot(x,y2)
plt.title("bawah barhart  cy2 vs x")
plt.show()

# Soal Ketujuh
labels = ['A', 'B', 'C']
y1 = [30, 40, 30]
plt.figure()
plt.pie(labels,y1,
        autopct='%1.1f%%')
plt.show()

# Soal Kedelapan
x = [1, 2, 3]
y1 = [1, 2, 3]
z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

plt.figure()
plt.plot_surface(x,y1,z)
plt.show()

# Soal Kesembilan
import numpy as np

x = np.linspace(0,2*np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

# Soal Kesepuluh
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x,y1,
         marker="o",
         color="blue",
         linewidth = 7)
plt.grid(True)
plt.title("Costume Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
