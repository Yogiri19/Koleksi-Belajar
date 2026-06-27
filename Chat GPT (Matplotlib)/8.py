import os
os.system("cls")
import matplotlib.pyplot as plt
import numpy as np

# DATA DASAR
x = np.arange(1,6)
y = x * 2

# STYLE BAWAAN
plt.style.use("ggplot")
plt.figure()
plt.plot(x,y)
plt.title("Style ggplot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# STYLE SEABORN
plt.style.use("seaborn-v0_8")
plt.figure()
plt.plot(x,y)
plt.title("style Seaborn")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# STYLE DARK BACKGROUND
plt.style.use("dark_background")
plt.figure()
plt.plot(x,y)
plt.title("Dark Background")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# COSTUM FONT SIZE
plt.style.use("default")
plt.figure()
plt.plot(x,y)
plt.title("Costum Font Size", fontsize=18)
plt.xlabel("X", fontsize=14)
plt.ylabel("Y", fontsize=14)
plt.show()

# COSTOM BACKGROUND & GRID
plt.figure()
plt.plot(x,y)
plt.title("Costum Background")
plt.gca().set_facecolor("#f2f2f2")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
