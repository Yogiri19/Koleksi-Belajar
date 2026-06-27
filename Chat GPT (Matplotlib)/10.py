import os
os.system('cls')

import matplotlib.pyplot as plt
import numpy as np

# DATA PENJUALAN 12 BULAN
bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
         "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]

penjualan = np.random.randint(50, 150, 12)
biaya = np.random.randint(30, 100, 12)
keuntungan = penjualan - biaya

# LINE CHART PENJUALAN
plt.figure(figsize=(8,4))
plt.plot(bulan, penjualan, marker="o", label="Penjualan")
plt.plot(bulan, biaya, marker="s", label="Biaya")
plt.title("Penjualan vs Biaya")
plt.xlabel("Bulan")
plt.ylabel("Jumlah")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# BAR CHART KEUNTUNGAN
plt.figure(figsize=(8, 4))
plt.bar(bulan, keuntungan, color="green")
plt.title("Keuntungan per bulan")
plt.xlabel("Bulan")
plt.ylabel("Keuntungan")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# HISTOGRAM DISTRIBUSI PENJUALAN
plt.figure()
plt.hist(penjualan, bins=5, edgecolor="black")
plt.title("Hubungan Penjualan dan biaya")
plt.xlabel("Penjualan")
plt.ylabel("Frekuensi")
plt.show()

# SCATTER HUBUNGAN Penjualan & Biaya
plt.figure()
plt.scatter(penjualan, biaya, s=100)
plt.title("Hubungan Penjualan dan Biaya")
plt.xlabel("Penjualan")
plt.ylabel("Biaya")
plt.grid(True)
plt.show()

# DASHBOARD SUBPLOT
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0,0].plot(bulan, penjualan)
axs[0,0].set_title("Penjualan")

axs[0,1].bar(bulan, keuntungan)
axs[0,1].set_title("Keuntungan")

axs[1,0].hist(penjualan, bins=5)
axs[1,0].set_title("Distribusi")

axs[1,1].scatter(penjualan, biaya)
axs[1,1].set_title("Relasi")

for ax in axs.flat:
    ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

fig.savefig("dashboard_penjualan.png", dpi=300)