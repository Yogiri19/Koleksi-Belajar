import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = x * 2

# FIGURE SIZE
plt.figure(figsize=(8,4)) # figsize = (lebar, tinggi)
plt.plot(x,y)
plt.title("Figure Size 8x4")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# FIGURE SIZE BESAR
plt.figure(figsize=(12,6)) # fig = (lebar, tinggi)
plt.plot(x,y)
plt.title("Figure Size 12x6")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# DPI (RESOLUSI)
plt.figure(figsize=(6, 4), dpi=150) # dpi = menjadi lebih tebal dan besar
plt.plot(x,y)
plt.title("Figure dengan DPI 150")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# TIGHT LAYOUT
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("Plot Atas")

plt.subplot(2,1,2)
plt.plot(x,y)
plt.title("Plot Bawah")

plt.tight_layout() # mengatur semuanya agar berjarak (label, judul,angka)
plt.show()

# SPACING MANUAL
plt.figure(figsize=(8,6))

plt.subplot(2, 1, 1)
plt.plot(x,y)
plt.title("Atas")

plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.title("Bawah")

plt.subplots_adjust(hspace=0.5) # Mengatur sublpot atas dam  bawah
plt.show()