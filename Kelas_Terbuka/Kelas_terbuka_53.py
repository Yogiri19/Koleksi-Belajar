import os
os.system("cls")
# ## global dan local scope

# nama_global = "otong" # <- ini variable global

# # akses variable global dalam fungsi
# def fungsi1():
#     print(f"fungsi menampilkan {nama_global}")
    
# fungsi1()

# # akses variable global dalam loop
# for i in range(0,3):
#     print(f"loop {i} - {nama_global}")


    
# # percabangan 
# nama_global = "otong" # <- ini variable global
# if True:
#     print(f"if menampilkan {nama_global}")
    
# ## variable local scope
# def fungsi2 ():
#     nama_lokal = "ucup" # <- variable lokal scop
                                  
# fungsi2()
# #print(nama_lokal)

# ## contoh 1: penggunaan
# def say_fahri():
#     print(f"hello {nama}")
    
# nama = "fahri" # si global nya duluan, ini bisa, karena sebelum say_fahri
# say_fahri()

# ## contoh 2 : merubah variable global
# angka = 0
# nama = "ucup"

# def ubah_angka(nilai_baru, nama_baru):
#     global angka #v fungsi ini mendapat akses merubah angka
#     global nama
#     angka = nilai_baru
#     nama = nama_baru
    
# print(f"sebelum = {angka,nama}")
# ubah_angka(10,"otong")
# print(f"sesudah = {angka,nama}")

# contoh 3:
print("=====")
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10
    
print(angka)
print(angka_dummy)

