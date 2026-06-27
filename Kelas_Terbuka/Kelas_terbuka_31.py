data_angka = [3,4,5,4,5,]

# count data
# menghitung berapa banyak angka di list
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)
data =["ucup", "dudung", "ujang"]
index_dudung = data.index("dudung")
index_ujang = data.index("ujang")
print(f"index si dudung = {index_dudung}")
print(f"index si ujang = {index_ujang}")

# mengurutkan list
data_angka.sort()
print(f"angka disort = {data_angka}")
data.sort()
print(f"data disort = {data}")

#balik listnya
data_angka.reverse()
data.reverse()
print(f"data sesudah reverse = {data_angka}, {data}")








