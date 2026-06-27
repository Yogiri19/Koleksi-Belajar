import matplotlib.pyplot as plt
import numpy as np

# DATA DASAR 
x = np.arange(1,6)
y = x ** 2

# SAVE PNG
plt.figure()
plt.plot(x,y)
plt.title("Save PNG")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafik_png.png")
plt.show()

# SAVE JPG DENGAN DPI TINGGI
plt.figure()
plt.plot(x,y)
plt.title("Save JPG DPI 300")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafik_jpg.jpg", dpi=300)
plt.show()

# SAVE PDF
plt.figure()
plt.plot(x,y)
plt.title("Save PDF")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafik_pdf.pdf")
plt.show()

# SAVE DENGAN BACKGROUND TRANSPARENT
plt.figure()
plt.plot(x,y)
plt.title("Transparent Background")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafik_transparant.png", transparent=True)
plt.show()

# SAVE DENGAN TIGHT LAYOUT
plt.figure()
plt.plot(x,y)
plt.title("Tight Layout Save")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.savefig("grafik_tight.png", bbox_inches="tight")
plt.show()