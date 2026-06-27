import os
os.system("cls")

import matplotlib.pyplot as plt

# # Soal Pertama
# x = [1, 2, 3, 4]
# y1 = [2, 4, 6, 8]
# y2 = [1, 3, 5, 7]

# plt.figure()
# plt.plot(x, y1, color="red")
# plt.plot(x, y2, color="blue")
# plt.title("Dua Warna")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Soal Kedua
# x = [0, 1, 2, 3]
# y1 = [1, 4, 9, 16]
# y2 = [16, 9, 4, 1]
# plt.figure()
# plt.plot(x, y1, marker="o")
# plt.plot(x, y2, marker="^")
# plt.title("Marker Berbeda")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # # Soal Ketiga
# x = [1, 2, 3, 4, 5]
# y1 = [3, 6, 9, 12, 15]
# y2 = [2, 5, 8, 11, 14]

# plt.figure()
# plt.plot(x, y1, color="green", marker="s")
# plt.plot(x, y2, color="black", marker="x")
# plt.title("Garis Berwarna dan Marker")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # # Soal Keempat
# x = [1, 2, 3, 4, 5]
# y1 = [5, 7, 6, 8, 9]
# y2 = [9, 8, 7, 6, 5]

# plt.figure()
# plt.plot(x, y1, color="red", marker="o")
# plt.plot(x, y2, color="black", marker="^")
# plt.title("Eksperimen Style")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Soal Kelima
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [10, 8, 6, 4, 2]

# plt.figure()
# plt.plot(x, y1, color="blue", marker="o")
# plt.plot(x, y2, color="red", marker="s")
# plt.title("Dua Pola Berlawanan")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]
# y3 = [5, 7, 6, 9, 2]

# plt.figure()
# plt.plot(x, y1, linestyle="--", color="green")
# plt.plot(x, y2, linestyle=":", color="blue")
# plt.plot(x, y3, linestyle="-.", color="blue")
# plt.title("Test")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


# # print("Soal Pertama")
# x = [1, 2, 3, 4]
# y1 = [2, 4, 6, 8]
# y2 = [1, 3, 5, 7]

# plt.figure()
# plt.plot(x, y1, linestyle="--")
# plt.plot(x, y2, linestyle=":")
# plt.title("Garis Berbeda")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Soal Kedua
# x = [0, 1, 2, 3]
# y1 = [1, 4, 9, 16]
# y2 = [16, 9, 4, 1]

# plt.figure()
# plt.plot(x, y1, linewidth=4)
# plt.plot(x, y2, linewidth=1)
# plt.title("Ketebalan Garis")
# plt.xlabel("X")

# plt.ylabel("Y")
# plt.show()      

# # Soal Ketiga
# x = [1, 2, 3, 4, 5]
# y1 = [3, 6, 9, 12, 15]
# y2 = [2, 5, 8, 11, 14]
# plt.figure()
# plt.plot(x, y1, linewidth=2, linestyle=":")
# plt.plot(x, y2, linewidth=4, linestyle="-.")
# plt.title("Dua Gaya")
# plt.xlabel("A")
# plt.ylabel("B")
# plt.legend()
# plt.show()

# # Soal Keempat
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]
# y3 = [5, 7, 6, 9, 12]

# plt.figure()
# plt.plot(x, y1, linewidth=2, linestyle=":")
# plt.plot(x, y2, linewidth=4, linestyle="--")
# plt.plot(x, y3, linewidth=6, linestyle="-.")
# plt.title("Tiga Data")
# plt.legend()
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Soal Kelima
# x = [1, 2, 3, 4, 5]
# y1 = [10, 8, 6, 4, 2]
# y2 = [2, 4, 6, 8, 10]
# y3 = [5, 6, 7, 8, 9]

# plt.figure()
# plt.plot(x, y1, linewidth=2, linestyle=":")
# plt.plot(x, y2, linewidth=4, linestyle="--")
# plt.plot(x, y3, linewidth=4, linestyle="-.")
# plt.title("Tiga Pola")
# plt.legend()
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]
# y3 = [5, 7, 6, 9, 12]

# plt.figure()
# plt.plot(x, y1, 
#          color="red", 
#          marker="o", #
#          linestyle="-", 
#          linewidth=2, 
#          label="Data A" )
# plt.plot(x, y2, 
#          color="blue", 
#          marker="s", 
#          linestyle="--", 
#          linewidth=2, 
#          label="Data B")
# plt.plot(x, y3, 
#          color="green", 
#          marker="^", 
#          linestyle=":", 
#          linewidth=2, 
#          label="Data C")
# plt.title("Warna + Marker + Line Style + Legend")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.grid(True)
# plt.show()

# Soal Pertama
x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [8, 6, 4, 2]

plt.figure()
plt.plot(x, y1, linestyle="--", linewidth= 2, color="red")
plt.plot(x, y2, linestyle="-.", linewidth= 3, color="green")
plt.legend()
plt.show()

# Soal Kedua
x = [1, 2, 3, 4, 5]
y1 = [1, 3, 5, 7, 9]
y2 = [2, 4, 6, 8, 10]
y3 = [5, 6, 7, 8, 9]

plt.figure()
plt.plot(x, y1,
          color="blue", 
          marker="o",
          label="A")
plt.plot(x, y2,
         color="red",
         marker="s",
         label="B")
plt.plot(x, y3,
         color="green",
         marker="x",
         label="C")
plt.legend()
plt.grid(True)
plt.show()

# Soal Ketiga
x = [0, 1, 2, 3]
y1 = [0, 1, 4, 9]
y2 = [9, 4, 1, 0]

plt.figure()
plt.plot(x, y1,
         linestyle="--",
         linewidth=1,
         label="A")
plt.plot(x, y2,
         linestyle=":",
         linewidth=2,
         label="B")
plt.legend()
plt.show()

# Soal Keempat
x = [1, 2, 3, 4, 5]
y1 = [3, 6, 9, 12, 15]
y2 = [2, 5, 8, 11, 14]
y3 = [1, 4, 6, 4, 2]

plt.figure()
plt.plot(x, y1,
         marker="o",
         color="red",
         linestyle="-.",
         label="A")
plt.plot(x, y2,
         marker="x",
         color="green",
         linestyle="--",
         label="B")
plt.plot(x, y3,
         marker="^",
         color="blue",
         linestyle=":",
         label="C")
plt.title("ini soal keempat")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

# Soal Kelima
x = [1, 2, 3, 4, 5, 6]
y1 = [2, 4, 6, 8, 10, 12]
y2 = [12, 10, 8, 6, 4, 2]
y3 = [3, 5, 7, 6, 8, 9]

plt.figure()
plt.plot(x, y1,
         color="red",
         marker="o",
         linestyle="--",
         linewidth=2,
         label="A")
plt.plot(x, y2,
         color="blue",
         marker="x",
         linestyle="-.",
         linewidth=3,
         label="B")
plt.plot(x, y3,
         color="green",
         marker="^",
         linestyle=":",
         linewidth=4,
         label="C")
plt.title("Soal Kelima")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()