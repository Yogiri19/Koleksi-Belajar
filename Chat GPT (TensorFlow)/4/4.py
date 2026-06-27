import tensorflow as tf

print(f"Versi: \n{tf.__version__}")

angka = tf.range(10)
print(angka)


angka = tf.range(
    start=0,
    limit=20,
    delta = 2
)
print(angka)

for i in tf.range(5):
    print(i.numpy())


for i in tf.range(5):
    print(i.numpy())


total = tf.Variable(0)
for i in tf.range(1, 11):
    total.assign_add(1)

print(f"Jumlah: \n{total.numpy()}")



nilai = tf.constant(80)
if nilai.numpy() >= 75:
    print(f"Lulus")
else:
    print(f"Tidak lulus")

nilai = tf.constant(80)

hasil = tf.cond(
    nilai >= 75,
    lambda: tf.constant("Lulus"),
    lambda: tf.constant("Tidak Lulus")
)

print(hasil.numpy().decode())



@tf.function
def tambah (a,b):
    return a + b

hasil = tambah(10, 20)
print(f"Hasil")


@tf.function
def hitung(a,b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b

    return tambah, kurang, kali, bagi

hasil = hitung(20.0, 5.0)
tf.print(hasil)


@tf.function
def jumlah(n):
    total = tf.constant(0)

    for i in tf.range(1, n + 1):
        total += i
    return total

print(jumlah(10))


@tf.function
def cek_nilai(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
print(cek_nilai(tf.constant(80)))


i = tf.constant(1)
total = tf.constant(0)

kondisi = lambda i, total: i <= 5
badan = lambda i, total: (
    i + 1,
    total + 1
)
i, total = tf.while_loop(
    kondisi,
    badan,
    [i, total]
)
print(total)


n = tf.constant(5)

i = tf.constant(1)
hasil = tf.constant(1)

kondisi = lambda i, hasil: i <= n
badan = lambda i, hasil: (
    i + 1,
    hasil * i
)

i, hasil = tf.while_loop(
    kondisi, 
    badan,
    [i, hasil]
)
print(f"Faktorial: \n{hasil}")


for i in tf.range(1,6):
    for j in tf.range(1, 6):
        hasil = i * j
        print(
            f"{i.numpy()} x {j.numpy()} = {hasil.numpy()}"
        )


nilai = tf.constant(
    [80, 70, 90, 85, 95]
)
jumlah = tf.constant(0)
for i in nilai:
    jumlah += i

rata_rata = (
    tf.cast(jumlah, tf.float32) / tf.cast(tf.size(nilai), tf.float32)
)

print(f"Jumlah: \n{jumlah}")
print(f"Rata-Rata: \n{rata_rata}")