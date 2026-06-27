# # Operator dalam bentuk method

# # merubah case dari string (wajib menggunakan "()" di akhir)

# # merubah semua ke upper case

# salam = "bro!"
# print("normal = " + salam)

# salam = salam.upper()
# print("upper = " + salam)

# # Merubah semua ke lower case
# nama = "Fakhri Dinal"
# print("normal =" + nama)
# nama = nama.lower()
# print("lower = " + nama)

# # pengecekan dengan menggunakan isX method

# # contoh pengecekan lower case
# salam = "fakhri"
# apakah_lower = salam.islower() #hasilnya bool
# print(salam +" is lower = " + str(apakah_lower))
# apakah_upper = salam.isupper() #hasilnya bool
# print(salam +" is upper = " + str(apakah_upper))

# # "()" gunanya untuk bool
# # isalpha() <-- untuk mengecek semuanya huruf
# nama = "Fakhri Dinal" # ini ada "spasi" jadinya akan false
# namaku = nama.isalpha()
# print(nama + " (isalpha) = " + str(namaku))

# # isalnum() <-- huruf dan angka
# nama = "Fakhri Dinal" # ini ada "spasi" jadinya akan false
# namaku = nama.isalnum()
# print(nama + " (isalnum) = " + str(namaku))

# # isdecimal() <--  angka saja
# nama = "Fakhri4 Dinal" #  False" = Karena ini ada "Huruf" dan "Spasi" 
# namaku = nama.isdecimal()
# print(nama + " (isdecimal) = " + str(namaku))

# # isspace()<-- spasi, tab, newline \n
# nama = "Fakhri Dinal"  # hanya berlaku untuk spasi, tab, newline \n
# namaku = nama.isspace() 
# print(nama + " (isspace) = " + str(namaku))

# # istitle <-- semua dimulai dengan huruf besar
# nama = "Fakhri Dinal"  # Karena "F" huruf besar jadinya "True"
# namaku = nama.istitle() 
# print(nama + " (istitle) = " + str(namaku))

# # ngecek komponen startwith() endswith() 
# cek_start = "Fakhri Dinal".startswith("Fak")
# print("start = " + str(cek_start))

# cek_end = "Fakhri Dinal".endswith("nal")
# print("end = " + str(cek_end))

# penggabungan Komponen join() split()
pisah = ['kiri','tengah','kanan']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
print("==========")
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = 'ehm'.join(pisah)
print(gabungan)

# gabungan = "akuehmsayangehmkamu"
# print(gabungan.split("ehm")) # Akan menjadi data list lagi

# # alokasi karakter rjust(), ljust() center()
# kanan = "kanan".rjust(10)
# print("'" +kanan+"'")

# kiri = "kiri".ljust(10)
# print("'" +kiri+"'")

# tengah = "tengah".center(10,":")
# print("'" +tengah+"'")

# #kebalikannya -> strip()
# tengah = tengah.strip(":") #menghilangkan tanda :
# print("'"+tengah+"'")
