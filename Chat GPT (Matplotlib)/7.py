import os
os.system('cls')

import matplotlib.pyplot as plt
import numpy as np

# DATA DASAR
x = np.arange(1, 11) # cetak dari 1 - 10
y = x ** 2
print(x)
print(y)
# BATAS AXIS
plt.figure()
plt.plot(x,y)
plt.xlim(0, 12) # kelipatan 2, 4, ...12
plt.ylim(0, 120) #  kelipatan 20, 40, ...120
plt.title("Batas Axis")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# COSTUM TICKS
plt.figure()
plt.plot(x,y)
plt.xticks([1, 3, 5, 7, 9]) # Mengcostum Jaraknya
plt.yticks([0, 20, 40, 50, 80, 100]) # Mengcostum jaraknya
plt.title("Costum Ticks")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ROTATE LABEL
kategori = ["Jan", "Feb", "Mar", "Apr", "Mei"]
nilai = [10, 15, 7, 20, 12]

plt.figure()
plt.bar(kategori, nilai)
plt.xticks(rotation=45) # Xlabel nya di miringin
plt.title("Rotate Label")
plt.xlabel("Bulan")
plt.ylabel("NIlai")
plt.show()

# LOG SCALE
plt.figure()
y_log = [1, 10, 100, 1000, 10000]
plt.plot([1, 2, 3, 4, 5], y_log)
plt.yscale("log")
plt.title("Log Scale")
plt.xlabel("X")
plt.ylabel("Y (Log)")
plt.show()

# TWINS AXIS
plt.figure()
fig, ax1 = plt.subplots()

ax1.plot(x,y,
         color="blue")
ax1.set_xlabel("X")
ax1.set_ylabel("Y Kuadrat", color="blue")

ax2 = ax1.twinx()
ax2.plot(x,x * 3, 
         color="red")
ax2.set_ylabel("Y Linear", color="red")

plt.title("Twin Axis")
plt.show()