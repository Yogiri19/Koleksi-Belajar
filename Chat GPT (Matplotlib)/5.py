import os
os.system("cls")

import matplotlib.pyplot as plt

# DATA DASAR
x = [1, 2, 3, 4, 5,]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 6, 7, 8, 9]

# SUBPLOT 1 BARIS 2 KOLOM
plt.figure()
plt.subplot(1, 2, 1) # (baris, kolom, posisi)
plt.plot(x,y1)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x,y2)
plt.title("Plot 2")
plt.show()

# SUBPLOT 2 BARIS 1 Kolom
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x,y1)
plt.title("Atas")

plt.subplot(2, 1, 2)
plt.plot(x,y2)
plt.title("bawah")
plt.show()

# SUBPLOT 2X2
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x,y1)
plt.title("A")

plt.subplot(2, 2, 2)
plt.plot(x,y2)
plt.title("B")

plt.subplot(2, 2, 3)
plt.plot(x,y3)
plt.title("C")

plt.subplot(2, 2, 4)
plt.plot(x,y1)
plt.title("D")
plt.show()

# SUBPLOTS (CARA MODEREN)
fig, axs = plt.subplots(2, 2) # Membuat 1 figure dan beberapa axs(grafik) 

axs[0, 0].plot(x,y1)
axs[0, 0].set_title("Plot 1")

axs[0, 1].plot(x, y2)
axs[0, 1].set_title("Plot 2")

axs[1, 0].plot(x, y3)
axs[1, 0].set_title("Plot 3")

axs[1, 1].plot(x, y1)
axs[1, 1].set_title("Plot 4")

plt.show()

