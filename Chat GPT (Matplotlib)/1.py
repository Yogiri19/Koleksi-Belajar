import os
os.system('cls')

import matplotlib.pyplot as plt

# DATA DASAR
x = [1, 2, 3, 4, 5] # Sumbu X Horizontal
y1 = [2, 4, 6, 8, 10] # Garis Pertama
y2 = [1, 3, 5, 7, 9] # Garis Kedua

# # PLOT SEDERHANA
# plt.figure()
# plt.plot(x, y1)
# plt.title("Plot Sederhana")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # PLOT + LABEL
# plt.figure()
# plt.plot(x, y1)
# plt.title("Grafik Pertumbuhan")
# plt.xlabel("Nilai X")
# plt.ylabel("Nilai Y")
# plt.show()

# PLOT + GRID
plt.figure()
plt.plot(x, y1)
plt.title("Grafik dengan grid")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# MULTIPLE LINE
plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Dua Garis dalam sati Grafik")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()