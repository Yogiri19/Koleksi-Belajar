import os

os.system('cls')
import tensorflow as tf

print("TensorFlow Version :", tf.__version__)

# CONSTANT TENSOR
a = tf.constant(10)
b = tf.constant(20)
print(a)
print(b)

# OPERASI DASAR
tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b

print("\nTambah :", tambah.numpy())
print("Kurang :", kurang.numpy())
print("Kali :", kali.numpy())
print("Bagi :", bagi.numpy())

# TENSOR VECTOR
vector = tf.constant([10, 20, 30, 40, 50])
print("\nVector")
print(vector)

# TENSOR MATRIX
matrix = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])
print("\nMatrix")
print(matrix)

# SHAPE
print("\nShape Vector :", vector.shape)
print("Shape Matrix :", matrix.shape)

# VARIABLE
nilai = tf.Variable(100)
print("\nNilai Awal :", nilai.numpy())
nilai.assign(200)
print("Nilai Baru :", nilai.numpy())

# LOOP
print("\nLoop Tensor")
for i in vector:
    print(i.numpy())

# IF ELSE
angka = tf.constant(80)
if angka.numpy() >= 75:
    print("\nLulus")
else:
    print("\nTidak Lulus")

# WHILE
counter = tf.Variable(1)
print("\nWhile Loop")
while counter.numpy() <= 5:
    print(counter.numpy())
    counter.assign_add(1)

# LATIHAN OPERASI
x = tf.constant(15)
y = tf.constant(5)
hasil1 = x + y
hasil2 = x - y
hasil3 = x * y
hasil4 = x / y
print("\nHasil Tambah :", hasil1.numpy())
print("Hasil Kurang :", hasil2.numpy())
print("Hasil Kali :", hasil3.numpy())
print("Hasil Bagi :", hasil4.numpy())





# # Soal Pertama
# import tensorflow as tf

# x = tf.constant(50)
# y = tf.constant(25)

# tambah = x + y
# kurang = x - y
# kali =  x * y
# bagi = x / y

# print(f"Tambah: \n{tambah.numpy()}\n")
# print(f"kurang: \n{kurang.numpy()}\n")
# print(f"kali: \n{kali.numpy()}\n")
# print(f"bagi: \n{bagi.numpy()}\n")

# # Soal Kedua
# import tensorflow as tf

# vector = tf.constant([5,10,15,20,25])
# print(f"Shape: {vector.shape}")
# for i in vector:
#     print(i.numpy())


# # Soal Ketiga
# import tensorflow as tf
# matrix = tf.constant([
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ])
# print(f"Matrix: \n{matrix.numpy()}\n")
# print(f"Shape Matrix: \n{matrix.shape}")

# # Soal Keempat
# import tensorflow as tf
# counter = tf.Variable(2)

# while counter.numpy() <= 10:
#     print(counter.numpy())
#     counter.assign_add(2)

# # Soal Kelima
# import tensorflow as tf

# nilai = tf.constant(85)
# if nilai.numpy() >= 75:
#     print(f"Lulus")
# else:
#     (f"Tidak lulus")

# vector = tf.constant([10,20,30,40])
# for i in vector.numpy():
#     print(f"{i}")

# print(f"\n")
# total = tf.Variable(0)

# while total.numpy() <= 10:
#     total.assign_add(4)
#     if total == i:
#         print(i)
#     else:
#         print()
