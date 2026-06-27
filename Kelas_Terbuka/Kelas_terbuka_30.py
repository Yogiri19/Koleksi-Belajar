# Operasi

# Index  0(-3)  1(-2)   2(-1)
data = ["ucup","otong","dudung"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"index 0  = {data_0}")

data_terakhir = data[-1]
print(f"data -1 = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list

# menambahkan item pada list sesuai posisi
data.insert(2,"asep")
print(f"di tambah = {data}")

# Menambah diakhir list
data.append("jajang")
print(f"ditambah diakhir = {data}")

# Menambahkan list dengan list
data_baru = ["ujang"]
data.extend(data_baru)
print(f"gabungan = {data}")

# Merubah data 
# Kita ubah data 2 dari asep menjadi michael
data[2] = "michael"
print(f"data rubah = {data}")

# Meremove data

data.remove("ujang")
print(f"data remove = {data}")

# meremove data paling belakang
data.pop()
print(f"data akhir = {data}")
