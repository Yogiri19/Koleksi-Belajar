import tensorflow as tf

print(f"Tensorflow Version: {tf.__version__}")

# Penjumlahan, Pengurangan, Perkalian, dan pembagian
a = tf.constant([10, 20, 30])
b = tf.constant([1, 2, 3])

print(f"a: {a}")
print(f"b: {b}")

print(f"Tambah: {a + b}")
print(f"kurang: {a - b}")
print(f"kali: {a * b}")
print(f"bagi: {a / b}")

# Fungsi Matematika TensorFlow
x = tf.constant([4.0, 9.0, 16.0])
print(f"Akar: {tf.sqrt(x)}")
print(f"Kuadrat: {tf.square(x)}")
print(f"Pangkat 3: {tf.pow(x,3)}")

# Nilai Minuimum dan maksimum
data = tf.constant([10, 50, 20, 90, 15])
print(f"Minimum: {tf.reduce_min(data)}")
print(f"Maksimum: {tf.reduce_max(data)}")

# Sum dan Mean
nilai = tf.constant([10, 20, 30, 40, 50])
print(f"Jumlah: {tf.reduce_sum(nilai)}")
print(f"Rata-Rata: {tf.reduce_mean(tf.cast(nilai,tf.float32))}")

# Matrix Addition
a = tf.constant([
    [1, 2],
    [3, 4]
])

b = tf.constant([
    [5, 6],
    [7, 8]
])

hasil = a + b
print(f"Hasil: \n{hasil}")

# Matrix Multiplication
a = tf.constant([
    [1, 2],
    [3, 4]
])
b = tf.constant([
    [5, 6],
    [7, 8]
])
hasil = tf.matmul(a,b)
print(f"hasil: \n{hasil}")

# Transpose Matrix
matrix = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"matrix: \n{matrix}")

transpose  = tf.transpose(matrix)
print(f"Transpose: \n{transpose}")

# Boardcasting dengan scalar
tensor = tf.constant([1, 2, 3, 4])
hasil = tensor + 10
print(f"Hasil: \n{hasil}")

# Boardcasting dengan Vector
matrix = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])
vector = tf.constant([10, 20, 30])
hasil = matrix + vector
print(f"Hasil: \n{hasil}")

# For Loop pada Tensor
tensor = tf.constant([10, 20, 30, 40, 50])
for i in tensor:
    print(i.numpy())