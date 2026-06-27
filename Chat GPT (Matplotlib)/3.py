# (82 + 85) / 2 = 83.5
import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np
# DATA BAR CHART
kategori = ["A", "B", "C", "D"]
nilai = [20, 35, 30, 15]

# BAR CHART VERTIKAL
plt.figure()
plt.bar(kategori, nilai)
plt.title("Bar Chart Vertikal")
plt.xlabel("Kategori")
plt.ylabel("Nilai")
plt.show()
# BAR CHART HORIZONTAL
plt.figure()
plt.barh(kategori, nilai)
plt.title("Bar Chart Horizontal")
plt.xlabel("Nilai")
plt.ylabel("Kategori")
plt.show()

# BAR CHART DENGAN WARNA
plt.figure()
plt.bar(kategori, nilai, color="orange")
plt.title("Bar Chart dengan Warna")
plt.xlabel("Kategori")
plt.ylabel("Nilai")
plt.show()

# DATA HISTOGRAM
data = np.random.randint(50, 100, 100) # (start, stop, jumlah)

# HISTOGRAM DASAR
plt.figure()
plt.hist(data)
plt.title("Histogram Dasar")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()

# HISTOGRAM DENGAN BINS
plt.figure()
plt.hist(data, bins=100) # bins = jarak antar batang
plt.title("Histogram dengan Bins")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()

# HISTOGRAM DENGAN EDGE & TRANSPARANSI
plt.figure()
plt.hist(data, bins=10, edgecolor="black", alpha=0.7)
plt.title("Histogram Lengkap")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()