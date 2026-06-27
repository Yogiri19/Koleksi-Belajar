import os
os.system("cls")

import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6, 7] # sumbu horizontal | Harus sama
# y1 = [2, 4, 6, 8, 10, 100, 1000] # Sumbu vertikal | Harus sama
# y2 = [1, 3, 5, 7, 9] 

# plt.figure() # buat grafik baru
# plt.plot(x, y1)
# plt.title("Plot Sederhana")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


# print("\nSoal Pertama")
# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]

# plt.figure()
# plt.plot(x, y)
# plt.title("Grafik Dasar")
# plt.ylabel("Y")
# plt.xlabel("X")
# plt.show()

# print("\nSoal Kedua")
# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]

# plt.figure()
# plt.plot(x,y)
# plt.title("Grafik Kuadrat")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# print("/nSoal Ketiga")

# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]

# plt.figure()
# plt.plot(x, y1, y2)
# plt.title("Perbandingan Dua Data")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# print("\nSoal Keempat")
# x = [1, 2, 3, 4, 5]
# y = [5, 3, 6, 2, 7]
# plt.figure()
# plt.grid()
# plt.plot(x,y)
# plt.title("Grafik dengan Grid")
# plt.show()

# print("\nSoal Kelima")

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 26]
# y2 = [25, 20, 12, 10, 5]

# plt.figure()
# plt.plot(x, y1, y2)
# plt.legend(x)
# plt.legend(y2)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

print("\nSoal Pertama")
x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

plt.figure()
plt.plot(x,y)
plt.title("Grafik Linear")
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
plt.show()

print("\nSoal Kedua")
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.figure()
plt.plot(x,y)
plt.title("Grafik Kuadrat")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# print("\nSoal Ketiga")
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Perbandingan Data")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("\nSoal Keempat")
x = [1, 2, 3, 4, 5]
y1 = [3, 6, 9, 12, 15]
y2 = [15, 12, 9, 6, 3]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Naik vs Turun")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("\nSoal Kelima")
x = [1, 2, 3, 4, 5]
y1 = [10, 8, 6, 4, 2]
y2 = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Perpotongan Harga")
plt.grid(True)
plt.show()

print("\nSoal Keenam")
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Naik Turun")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("\nSoal Ketujuh")
x = [2, 4, 6, 8]
y1 = [1, 3, 5, 7]
y2 = [7, 5, 3, 1]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Simetri Data")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("\nSoal Kedelapan")
x = [0, 2, 4, 6, 8]
y1 = [0, 5, 10, 15, 20]
y2 = [20, 15, 10, 5, 0]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Dua Arah")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("\nSoal Kesepuluh")
x = [1, 2, 3, 4, 5]
y1 = [3, 6, 9, 12, 15]
y2 = [2, 5, 8, 11, 14]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Dua tren")
plt.grid(True)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y1, label="Tren 1")
plt.plot(x, y2, label="Tren 2")
plt.show()

