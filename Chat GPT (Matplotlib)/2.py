import os
os.system("cls")

import matplotlib.pyplot as plt

# Color -> Warna garis
# Marker -> Bentuk Titik
# Linestyle -> Jenis Garis
# Linewidth -> Ketebalan
# Label + Legend() -> Keterangan Grafik
# DATA DASAR
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 7, 6, 9, 12]

# WARNA GARIS
plt.figure()
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="blue")
plt.title("Warna Garis")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# MARKER
plt.figure()
plt.plot(x, y1, marker="o")
plt.plot(x, y2, marker="s")
plt.title("Maker")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# LINE STYLE
plt.figure()
plt.plot(x, y1, linestyle="--")
plt.plot(x, y2, linestyle=":")
plt.title("Line Style")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# LINE WIDTH
plt.figure()
plt.plot(x, y1, linewidth=3)
plt.plot(x, y2, linewidth=1)
plt.title("Line Width")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# LEGEND
plt.figure()
plt.plot(x, y1, label="Data A")
plt.plot(x, y2, label="Data B")
plt.plot(x, y3, label="Data C")
plt.title("Legend")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# GABUNGKAN SEMUA
plt.figure()
plt.plot(x, y1, 
         color="red",# Warna Merah
         marker="o", # titik bulat
         linestyle="-", # garis penuh default
         linewidth=2, # ketebalan
         label="Data A" ) # teks legend
plt.plot(x, y2, 
         color="blue", 
         marker="s", 
         linestyle="--", 
         linewidth=2, 
         label="Data B")
plt.plot(x, y3, 
         color="green", 
         marker="^", 
         linestyle=":", 
         linewidth=2, 
         label="Data C")
plt.title("Warna + Marker + Line Style + Legend")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True) # Garis bantu latar belakang
plt.show()