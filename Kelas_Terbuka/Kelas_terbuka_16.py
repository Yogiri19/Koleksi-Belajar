# operasi dan manipulasi string

# 1. menyambung string(concatenate)
nama_pertama = "Fakhri"
nama_tengah = "D"
nama_akhir = "Maulana"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string (jadi + dan , itu sama saling menghubungkan)
panjang = len(nama_lengkap) #Spasi juga dihitung
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string 

d = "d"
status = d in nama_lengkap
print (d + " ada di " + nama_lengkap + " = " + str(status)) 

D = "D"
status = D in nama_lengkap
print (D + " ada di " + nama_lengkap + " = " + str(status)) 

d = "d"
status = d not in nama_lengkap
print (d + " tidak ada di " + nama_lengkap + " = " + str(status)) 

# Mengulang string
print(15*"wk")
print("wk"*15)

#indexing
print("index ke-0 :" + nama_lengkap[0]) #ini memulai dari "F" karna "F" itu 0
print("index ke-6 :" + nama_lengkap[6]) 
print("index ke-[-1] :" + nama_lengkap[-1]) #Kalo "-1" itu ngambil dari belakang jadinya "a"
print("index ke-[-2] :" + nama_lengkap[-2]) 
print("index ke-[0:3]:" + nama_lengkap[0:4])  # : itu adalah sampai
print("index ke-[3:7] :" + nama_lengkap[3:8])  
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:10:2]) # Dimulai dari 2 dan ke "11" menggunakan pembagian langkah yang diambil "2"

#item paling kecil (dari alfabet)
print("print paling kecil :" + min(nama_lengkap))

#item paling besar (dari alfabet)
print("print paling besar :" + max(nama_lengkap))

ascii_code = ord("u")
print("ASCII code untuk u adalah " + str(ascii_code)) # ASCII itu mengambil dari sananya
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4.Operator dalam bentuk method

data = "FakhriDMaulana"
jumlah = data.count("a") # "count" adalah menghitung "a" 
print("jumlah a pada " + data + " = " + str(jumlah)) # Integer nya harus diubah ke String


