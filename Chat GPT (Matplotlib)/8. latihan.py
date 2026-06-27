import os
os.system("cls")

import numpy as np
import matplotlib.pyplot as plt

# Soal Pertama
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

plt.style.use("ggplot")
plt.figure()
plt.plot(x,y1)
plt.title("Latihan Style ggplot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Soal Kedua
x = [0, 1, 2, 3, 4]
y1 = [1, 1, 2, 3, 5]

plt.style.use("seaborn-v0_8")
plt.figure()
plt.plot(x,y1)
plt.title("Style Seaborn")
plt.show()

# Soal Ketiga
x = [1, 2, 3, 4, 5]
y1 = [5, 4, 3, 2, 1]

plt.style.use("dark_background")
plt.figure()
plt.plot(x,y1)
plt.title("Dark Theme")
plt.show()

# Soal Keempat
x = [1, 2, 3, 4, 5]
y1 = [3, 6, 9, 12, 15]

plt.style.use("default")
plt.figure()
plt.plot(x,y1)
plt.title("default", fontsize=18)
plt.xlabel("X", fontsize=14)
plt.ylabel("Y", fontsize=14)
plt.show()

# Soal Kelima
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x,y1)
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_facecolor("#f2f2f2")
plt.show()

# Soal Keenam
x = [0, 2, 4, 6, 8]
y1 = [0, 1, 0, 1, 0]
y2 = [1, 0, 1, 0, 1]

plt.figure()
plt.style.use("ggplot")
plt.subplot(2, 1, 1)
plt.plot(x,y1)

plt.style.use("default")
plt.subplot(2, 1, 2)
plt.plot(x,y2)
plt.show()

# Soal Ketujuh
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

plt.style.use("dark_background")
plt.figure()
plt.plot(x,y1,
         marker="o",)
plt.title("Dark + Grid + Marker")
plt.grid(True)
plt.show()

# Soal Kedelapan
x = [1, 2, 3, 4, 5]
y1 = [1, 8, 27, 64, 125]
y2 = [1, 4, 9, 16, 25]

plt.figure()
plt.style.use("ggplot")
plt.subplot(2, 1, 1)
plt.plot(x,y1)

plt.subplot(2, 1, 2)
plt.plot(x,y2)
plt.grid(True, linestyle="--", alpha=0.5)
plt.gca().set_facecolor("#f2f2f2")
plt.tight_layout()
plt.show()

# Soal Kesembilan
x = [1, 2, 3, 4, 5, 6]
y1 = [2, 3, 5, 7, 11, 13]
y2 = [1, 1, 2, 3, 5, 8]

plt.figure() 
fig,ax1 = plt.subplots()
ax1.plot(x,y1,
         color="blue")
plt.title("Twin Axis Styled")
ax1.set_ylabel("Prima", color="blue")

ax2 = ax1.twinx()
ax2.plot(x,y2,
         color="red")
ax2.set_ylabel("Fibonacci", color="red")
plt.show()

# Soal Kesepuluh
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [30, 25, 20, 15, 10]
y3 = [12, 18, 22, 19, 24]

plt.style.use("default")
plt.style.use("dark_background")
plt.figure(figsize=(8,10))
plt.subplot(3, 1, 1)
plt.plot(x,y1,
         marker="o")

plt.subplot(3, 1, 2)
plt.plot(x,y2)
plt.grid(True)
plt.gca().set_facecolor("#f8f8ff")

plt.subplot(3, 1, 3)
plt.plot(x,y3)
plt.tight_layout()
plt.show()

