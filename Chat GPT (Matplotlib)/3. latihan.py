import os
os.system("cls")

import matplotlib.pyplot as plt
import numpy as np

# # DATA BAR CHART

# kategori = ["A", "B", "C", "D"]
# nilai = [20, 35, 30, 15]

# # BAR CHART VERTIKAL
# plt.figure()
# plt.bar(kategori, nilai)
# plt.title("Bar Chart Vertikal")
# plt.xlabel("Kategori")
# plt.ylabel("Nilai")
# plt.show()

# # BAR CHART HORIZONTAL
# plt.figure()
# plt.barh(kategori, nilai)
# plt.title("Bar Chart Horizontal")
# plt.xlabel("Nilai")
# plt.ylabel("Kategori")
# plt.show()

# # BAR CHART DENGAN WARNA
# plt.figure()
# plt.bar(kategori, nilai, color="orange")
# plt.title("Bar Chart dengan Warna")
# plt.xlabel("Kategori")
# plt.ylabel("Nilai")
# plt.show()

# # BAR WARNA BERBEDA
# plt.figure()
# plt.bar(kategori, nilai, color=["red", "blue", "green", "orange"])
# plt.title("Ini Warna berbeda")
# plt.show()


# # Soal Pertama
# kategori = ["P", "Q", "R"] 
# nilai = [10, 25, 15]
# plt.figure()
# plt.barh(kategori, nilai)
# plt.title("soal pertama")
# plt.xlabel("Y")
# plt.ylabel("X")
# plt.show()

# # Soal kedua
# kategori = ["Jan", "Feb", "Mar", "Apr"]
# nilai = [40, 30, 50, 20]
# plt.figure()
# plt.bar(kategori, nilai)
# plt.show()

# # Soal Ketiga
# kategori = ["A", "B", "C"]
# nilai = [5, 15, 25]
# plt.figure()
# plt.barh(kategori, nilai,
#          color="purple")
# plt.show()

# # Soal Keempat
# kategori = ["X", "Y", "Z"]
# nilai = [12, 22, 18]
# plt.figure()
# plt.bar(kategori, nilai, 
#         color=["red", "black", "yellow"])
# plt.show()

# # Soal Kelima
# kategori = ["satu", "Dua", "Tiga"]
# nilai = [30, 10, 20]
# plt.figure()
# plt.bar(kategori, nilai,
#         color="red")
# plt.show()

# # Soal Keenam
# kategori = ["A", "B", "C", "D"]
# nilai = [15, 25, 10, 30]
# plt.figure()
# plt.bar(kategori, nilai)
# plt.barh(kategori, nilai)
# plt.show()

# # Soal Ketujuh
# kategori = ["K1", "K2", "K3", "K4"]
# nilai = [8, 16, 24, 12]
# plt.figure()
# plt.bar(kategori, nilai,
#         color=["blue", "red", "yellow", "green"])
# plt.title("Soal Ketujuh")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Saol Kedelapan
# kategori = ["L", "M", "N"]
# nilai = [14, 21, 7]
# plt.figure()
# plt.bar(kategori, nilai,
#         color="green")
# plt.show()

# # Soal Kesembilan
# kategori = ["ab", "cd", "ef", "gh", "ij"]
# nilai = [11, 22, 33, 44, 55]
# plt.figure()
# plt.barh(kategori, nilai,
#          color=["blue", "red", "grey", "pink", "cyan"])
# plt.title("Soal Kesembilan")
# plt.show()

# # Soal Kesepuluh
# kategori = ["Produk1", "Produk2", "Produk3", "Produk4"]
# nilai = [45, 30, 20, 50]
# plt.figure()
# plt.bar(kategori, nilai,
#         color="red")
# plt.barh(kategori, nilai,
#          color=["red", "blue", "cyan", "yellow", "black"])
# plt.show()

# Soal Pertama
data = [60, 65, 70, 75, 80, 85, 90]
plt.figure()
plt.hist(data)
plt.title("Soal Pertama")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Soal Kedua
data = np.random.randint(0, 100, 50)
plt.figure()
plt.hist(data)
plt.show()

# Soal Ketiga
data = np.random.randint(10, 60, 100)
plt.figure()
plt.hist(data,
         bins=5)
plt.show()

# Soal keempat
data = [10, 20, 30, 40]
plt.figure()
plt.hist(data,
         bins=10,
         edgecolor="black")
plt.show()

# Soal Kelima
data = [10, 20, 30, 40, 50]
plt.figure()
plt.hist(data,
         bins=15,
         alpha=0.5)
plt.show()

# Soal Keenam
data = [11, 22, 33, 44, 55]
plt.figure()
plt.hist(data,
         bins=8,
         edgecolor="black",
         alpha=0.6)
plt.show()

# Soal Ketujuh
data = np.random.randint(1, 100, 200)
plt.figure()
plt.hist(data,
         bins=20)
plt.show()

# Soal Kedelapan
data = [11, 22, 33, 44, 55]
plt.figure()
plt.hist(data,
         bins=12,
         edgecolor="black",
         alpha=0.4)
plt.show()

# Soal Kesembilan
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
         11, 22, 33, 44, 55, 66, 77, 88, 99, 00,
         111, 222, 333, 444, 555, 666, 777, 888, 999, 000]
plt.figure()
plt.hist(data,
         bins=99)
plt.title("Soal Kesepuluh")
plt.show()

# Soal Kesepuluh
data = [11, 22, 33, 44, 55]
plt.figure()
plt.hist(data,
         bins=10)
plt.hist(data,
         bins=10)
plt.show()